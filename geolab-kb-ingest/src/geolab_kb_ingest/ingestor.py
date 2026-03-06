"""Orchestrator: chunk -> embed -> store."""

from __future__ import annotations

import json
from pathlib import Path

from rich.console import Console
from rich.progress import Progress
from sqlalchemy import Engine

from .chunker import Chunk, _count_tokens, chunk_package
from .db import KBChunk, bulk_insert_chunks, delete_package_chunks, get_session
from .embedder import Embedder


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
        discipline=chunk.discipline,
        level=chunk.level,
        token_count=_count_tokens(chunk.content),
    )


def ingest_package(
    package_dir: Path,
    engine: Engine,
    embedder: Embedder,
    console: Console,
    max_tokens: int = 1500,
) -> int:
    """Ingest one package. Returns chunk count. Atomic transaction."""
    manifest_path = package_dir / "_manifest.json"
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    package_id = manifest["id"]
    console.print(f"  Chunking [bold]{manifest['name']}[/bold] ...")

    chunks = chunk_package(package_dir, max_tokens=max_tokens)
    if not chunks:
        console.print("  [yellow]No chunks produced.[/yellow]")
        return 0

    console.print(f"  Embedding {len(chunks)} chunks ...")
    texts = [c.content for c in chunks]
    embeddings = embedder.embed_texts(texts)

    db_chunks = [
        _chunk_to_db(chunk, emb) for chunk, emb in zip(chunks, embeddings)
    ]

    with get_session(engine) as session:
        deleted = delete_package_chunks(session, package_id)
        if deleted:
            console.print(f"  Replaced {deleted} existing chunks.")
        bulk_insert_chunks(session, db_chunks)

    console.print(f"  [green]Stored {len(db_chunks)} chunks.[/green]")
    return len(db_chunks)


def _discover_packages(packages_dir: Path) -> list[Path]:
    """Find all package directories (folders containing _manifest.json)."""
    return sorted(
        p.parent for p in packages_dir.rglob("_manifest.json")
    )


def ingest_all(
    packages_dir: Path,
    engine: Engine,
    embedder: Embedder,
    ordered: bool,
    console: Console,
    max_tokens: int = 1500,
) -> dict:
    """Ingest all packages. Returns stats dict."""
    pkg_dirs = _discover_packages(packages_dir)

    if ordered:
        # Sort by level (read manifest to get level)
        def _get_level(d: Path) -> int:
            try:
                with open(d / "_manifest.json", encoding="utf-8") as f:
                    return json.load(f).get("level", 0)
            except Exception:
                return 99
        pkg_dirs.sort(key=_get_level)

    stats = {"total_packages": len(pkg_dirs), "total_chunks": 0, "errors": []}

    with Progress(console=console) as progress:
        task = progress.add_task("Ingesting packages", total=len(pkg_dirs))
        for pkg_dir in pkg_dirs:
            try:
                count = ingest_package(
                    pkg_dir, engine, embedder, console, max_tokens=max_tokens
                )
                stats["total_chunks"] += count
            except Exception as e:
                err_msg = f"{pkg_dir.name}: {e}"
                console.print(f"  [red]Error: {err_msg}[/red]")
                stats["errors"].append(err_msg)
            progress.advance(task)

    return stats
