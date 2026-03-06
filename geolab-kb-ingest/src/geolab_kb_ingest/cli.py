"""Click CLI for GeoLab KB Ingest."""

from __future__ import annotations

import io
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from sqlalchemy import func

from .config import get_settings
from .db import KBChunk, get_engine, get_session, init_db
from .doc_ingestor import ingest_documents
from .embedder import Embedder
from .ingestor import ingest_all, ingest_package
from .query import query_chunks
from .validator import validate_all, validate_package

# Force UTF-8 output on Windows to handle Greek/math symbols in content
if sys.platform == "win32" and not isinstance(sys.stdout, io.TextIOWrapper):
    pass  # Already wrapped
elif sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

console = Console(force_terminal=True)


def _make_engine():
    settings = get_settings()
    engine = get_engine(settings.database_url)
    init_db(engine)
    return engine, settings


def _make_embedder(settings):
    return Embedder(
        api_key=settings.voyage_api_key,
        model=settings.voyage_model,
        batch_size=settings.voyage_batch_size,
        dims=settings.embedding_dims,
    )


@click.group()
def cli():
    """GeoLab Knowledge Base Ingest Tool."""


@cli.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def ingest(path: Path):
    """Ingest a single knowledge package."""
    engine, settings = _make_engine()
    embedder = _make_embedder(settings)
    count = ingest_package(
        path, engine, embedder, console, max_tokens=settings.chunk_max_tokens
    )
    console.print(f"\n[bold green]Done — {count} chunks ingested.[/bold green]")


@cli.command("ingest-all")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
@click.option("--ordered", is_flag=True, help="Ingest in level order (0 → 1 → 2).")
def ingest_all_cmd(path: Path, ordered: bool):
    """Ingest all knowledge packages from a directory."""
    engine, settings = _make_engine()
    embedder = _make_embedder(settings)
    stats = ingest_all(
        path, engine, embedder, ordered, console, max_tokens=settings.chunk_max_tokens
    )
    console.print(
        f"\n[bold green]Done — {stats['total_chunks']} chunks "
        f"from {stats['total_packages']} packages.[/bold green]"
    )
    if stats["errors"]:
        console.print(f"[red]{len(stats['errors'])} errors occurred.[/red]")


@cli.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def reingest(path: Path):
    """Re-ingest a package (idempotent — replaces existing chunks)."""
    engine, settings = _make_engine()
    embedder = _make_embedder(settings)
    count = ingest_package(
        path, engine, embedder, console, max_tokens=settings.chunk_max_tokens
    )
    console.print(f"\n[bold green]Done — {count} chunks re-ingested.[/bold green]")


@cli.command()
@click.argument("text")
@click.option("--type", "chunk_type", help="Filter by chunk type.")
@click.option("--top-k", default=5, help="Number of results.")
@click.option("--discipline", help="Filter by discipline.")
def query(text: str, chunk_type: str | None, top_k: int, discipline: str | None):
    """Search the knowledge base by similarity."""
    engine, settings = _make_engine()
    embedder = _make_embedder(settings)
    results = query_chunks(
        engine, embedder, text, top_k=top_k,
        chunk_type=chunk_type, discipline=discipline,
    )

    if not results:
        console.print("[yellow]No results found.[/yellow]")
        return

    table = Table(title="Search Results", show_lines=True)
    table.add_column("Score", style="cyan", width=6)
    table.add_column("Type", style="magenta", width=10)
    table.add_column("Title", style="bold")
    table.add_column("Package", style="dim")
    table.add_column("Content", max_width=60)

    for r in results:
        content_preview = r["content"][:200] + "..." if len(r["content"]) > 200 else r["content"]
        table.add_row(
            f"{r['score']:.3f}",
            r["chunk_type"],
            r["title"],
            r["package_id"],
            content_preview,
        )

    console.print(table)


@cli.command()
@click.option("--package", help="Filter by package ID.")
def stats(package: str | None):
    """Show chunk statistics."""
    engine, settings = _make_engine()

    with get_session(engine) as session:
        # Total count
        total = session.query(func.count(KBChunk.id)).scalar() or 0
        console.print(f"\n[bold]Total chunks:[/bold] {total}")

        # By type
        type_rows = (
            session.query(KBChunk.chunk_type, func.count(KBChunk.id))
            .group_by(KBChunk.chunk_type)
            .order_by(KBChunk.chunk_type)
            .all()
        )
        if type_rows:
            table = Table(title="Chunks by Type")
            table.add_column("Type", style="magenta")
            table.add_column("Count", style="cyan", justify="right")
            for ct, count in type_rows:
                table.add_row(ct, str(count))
            console.print(table)

        # By discipline
        disc_rows = (
            session.query(KBChunk.discipline, func.count(KBChunk.id))
            .group_by(KBChunk.discipline)
            .order_by(KBChunk.discipline)
            .all()
        )
        if disc_rows:
            table = Table(title="Chunks by Discipline")
            table.add_column("Discipline", style="green")
            table.add_column("Count", style="cyan", justify="right")
            for disc, count in disc_rows:
                table.add_row(disc, str(count))
            console.print(table)

        # By package (optional filter)
        pkg_query = (
            session.query(KBChunk.package_id, func.count(KBChunk.id))
            .group_by(KBChunk.package_id)
            .order_by(KBChunk.package_id)
        )
        if package:
            pkg_query = pkg_query.filter(KBChunk.package_id == package)

        pkg_rows = pkg_query.all()
        if pkg_rows:
            table = Table(title="Chunks by Package")
            table.add_column("Package ID", style="bold")
            table.add_column("Count", style="cyan", justify="right")
            for pid, count in pkg_rows:
                table.add_row(pid, str(count))
            console.print(table)


@cli.command("ingest-docs")
@click.argument("path", type=click.Path(exists=True, path_type=Path))
@click.option("--project", default="Juniper Canyon Dam", help="Project name for metadata tagging.")
@click.option("--max-tokens", default=512, help="Max tokens per narrative chunk.")
@click.option("--overlap", default=50, help="Token overlap between chunks.")
def ingest_docs_cmd(path: Path, project: str, max_tokens: int, overlap: int):
    """Ingest raw PDF/CSV documents from a directory."""
    engine, settings = _make_engine()
    embedder = _make_embedder(settings)
    count = ingest_documents(
        path,
        engine,
        embedder,
        console,
        project_name=project,
        max_tokens=max_tokens,
        overlap_tokens=overlap,
    )
    console.print(f"\n[bold green]Done — {count} chunks ingested from documents.[/bold green]")


@cli.command()
@click.argument("path", type=click.Path(exists=True, path_type=Path))
def validate(path: Path):
    """Validate package structure."""
    # Single package or directory of packages?
    if (path / "_manifest.json").exists():
        errors = validate_package(path)
        if errors:
            console.print(f"[red]{path.name}: {len(errors)} error(s)[/red]")
            for e in errors:
                console.print(f"  - {e}")
        else:
            console.print(f"[green]{path.name}: OK[/green]")
    else:
        results = validate_all(path)
        # Count total packages
        total = len(list(path.rglob("_manifest.json")))
        ok = total - len(results)
        console.print(
            f"\n[bold]Validated {total} packages:"
            f" {ok} OK, {len(results)} with errors.[/bold]"
        )
        for pkg_path, errors in sorted(results.items()):
            console.print(f"\n[red]{pkg_path}:[/red]")
            for e in errors:
                console.print(f"  - {e}")
        if not results:
            console.print("[green]All packages valid![/green]")
