"""Orchestrator for raw document ingestion (PDF/CSV -> chunks -> embed -> store).

Unlike the package ingestor (ingestor.py) which processes structured knowledge
packages, this module handles arbitrary PDF/CSV document directories.
"""
from __future__ import annotations

from pathlib import Path

from rich.console import Console
from rich.progress import Progress
from sqlalchemy import Engine

from .chunker import Chunk, _count_tokens
from .db import KBChunk, bulk_insert_chunks, delete_package_chunks, get_session
from .doc_chunker import (
    chunk_document,
    extract_csv_text,
    extract_doc_metadata,
    extract_pdf_pages,
)
from .embedder import Embedder


def _slugify_project(name: str) -> str:
    """Convert project name to a package_id slug."""
    import re

    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return f"project:{slug.strip('-')}"


def _chunk_to_db(chunk: Chunk, embedding: list[float]) -> KBChunk:
    """Convert a Chunk dataclass + embedding vector to a KBChunk ORM object."""
    return KBChunk(
        id=chunk.id,
        package_id=chunk.package_id,
        chunk_type=chunk.chunk_type,
        title=chunk.title,
        content=chunk.content,
        embedding=embedding,
        metadata_=chunk.metadata,
        tags=chunk.tags,
        discipline=chunk.discipline or "project-data",
        level=chunk.level,
        token_count=_count_tokens(chunk.content),
    )


def ingest_documents(
    docs_dir: Path,
    engine: Engine,
    embedder: Embedder,
    console: Console,
    *,
    project_name: str = "Juniper Canyon Dam",
    package_id: str | None = None,
    max_tokens: int = 512,
    overlap_tokens: int = 50,
) -> int:
    """Ingest all PDF/CSV files from a directory into the KB.

    Args:
        docs_dir: Directory containing PDF/CSV files.
        engine: SQLAlchemy engine.
        embedder: Voyage AI embedder.
        console: Rich console for output.
        project_name: Human-readable project name.
        package_id: Override package namespace (default: derived from project_name).
        max_tokens: Max tokens per narrative chunk.
        overlap_tokens: Token overlap between chunks.

    Returns:
        Total number of chunks stored.
    """
    if package_id is None:
        package_id = _slugify_project(project_name)

    tags = [project_name.lower().replace(" ", "-")]

    # Discover files
    pdf_files = sorted(docs_dir.glob("*.pdf"))
    csv_files = sorted(docs_dir.glob("*.csv"))
    all_files = pdf_files + csv_files

    if not all_files:
        console.print("[yellow]No PDF or CSV files found.[/yellow]")
        return 0

    console.print(
        f"Found [bold]{len(pdf_files)}[/bold] PDFs and "
        f"[bold]{len(csv_files)}[/bold] CSVs in {docs_dir}"
    )

    # Extract and chunk all files
    all_chunks: list[Chunk] = []

    with Progress(console=console) as progress:
        task = progress.add_task("Extracting & chunking", total=len(all_files))

        for file_path in all_files:
            ext = file_path.suffix.lower()

            try:
                if ext == ".pdf":
                    pages = extract_pdf_pages(file_path)
                    full_text = "\n\n".join(p["text"] for p in pages)
                    doc_meta = extract_doc_metadata(full_text, file_path.name)
                    doc_meta["pages"] = len(pages)
                    doc_meta["project"] = project_name

                    chunks = chunk_document(
                        full_text,
                        doc_meta,
                        package_id,
                        max_tokens=max_tokens,
                        overlap_tokens=overlap_tokens,
                        tags=tags,
                    )

                elif ext == ".csv":
                    text = extract_csv_text(file_path)
                    doc_meta = {
                        "filename": file_path.name,
                        "title": file_path.stem.replace("_", " ").title(),
                        "project": project_name,
                    }

                    chunks = chunk_document(
                        text,
                        doc_meta,
                        package_id,
                        tags=tags,
                        is_csv=True,
                    )
                else:
                    progress.advance(task)
                    continue

                all_chunks.extend(chunks)
                console.print(
                    f"  {file_path.name}: {len(chunks)} chunks"
                )

            except Exception as e:
                console.print(f"  [red]Error processing {file_path.name}: {e}[/red]")

            progress.advance(task)

    if not all_chunks:
        console.print("[yellow]No chunks produced.[/yellow]")
        return 0

    console.print(f"\n[bold]Total: {len(all_chunks)} chunks from {len(all_files)} files[/bold]")

    # Embed all chunks
    console.print("Embedding chunks via Voyage AI ...")
    texts = [c.content for c in all_chunks]
    embeddings = embedder.embed_texts(texts)

    # Convert to DB objects
    db_chunks = [
        _chunk_to_db(chunk, emb)
        for chunk, emb in zip(all_chunks, embeddings)
    ]

    # Store atomically
    console.print("Storing in database ...")
    with get_session(engine) as session:
        deleted = delete_package_chunks(session, package_id)
        if deleted:
            console.print(f"  Replaced {deleted} existing chunks for {package_id}")
        bulk_insert_chunks(session, db_chunks)

    console.print(f"[bold green]Done — {len(db_chunks)} chunks stored as {package_id}[/bold green]")
    return len(db_chunks)
