"""Table-aware token-based chunker for raw PDF/CSV documents.

Unlike the knowledge-package chunker (chunker.py) which processes structured
packages with manifest/theory/equations/tables/standards, this module handles
raw document files (PDFs, CSVs) by extracting text and producing Chunk objects
suitable for embedding and storage.
"""
from __future__ import annotations

import csv
import io
import re
from pathlib import Path

import tiktoken

from .chunker import Chunk

_ENC = tiktoken.get_encoding("cl100k_base")


def _count_tokens(text: str) -> int:
    """Count tokens using cl100k_base encoding."""
    return len(_ENC.encode(text))


# ---------------------------------------------------------------------------
# PDF extraction
# ---------------------------------------------------------------------------

def extract_pdf_pages(file_path: Path) -> list[dict]:
    """Extract text from a PDF using pdfplumber, marking table regions.

    Returns list of dicts: {page: int, text: str}
    Table regions are wrapped in [TABLE]...[/TABLE] markers.
    """
    import pdfplumber

    pages: list[dict] = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text() or ""
            tables = page.extract_tables()
            table_text = ""
            for table in tables:
                if table:
                    rows_text = []
                    for row in table:
                        cleaned = [str(cell) if cell else "" for cell in row]
                        rows_text.append(" | ".join(cleaned))
                    table_text += "\n[TABLE]\n" + "\n".join(rows_text) + "\n[/TABLE]\n"

            combined = page_text
            if table_text:
                combined += table_text

            pages.append({"page": i + 1, "text": combined})

    return pages


# ---------------------------------------------------------------------------
# CSV extraction
# ---------------------------------------------------------------------------

def extract_csv_text(file_path: Path) -> str:
    """Extract text from a CSV as pipe-delimited rows."""
    raw = file_path.read_text(encoding="utf-8", errors="replace")
    reader = csv.reader(io.StringIO(raw))
    rows = list(reader)
    if not rows:
        return ""
    header = rows[0]
    lines = [" | ".join(header)]
    lines.append("-" * len(lines[0]))
    for row in rows[1:]:
        lines.append(" | ".join(row))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Metadata extraction
# ---------------------------------------------------------------------------

def extract_doc_metadata(text: str, filename: str) -> dict:
    """Extract title, author/firm, and date from the first page text.

    Uses common patterns found in geotechnical reports.
    """
    meta: dict = {"filename": filename}

    # Title — first non-empty line that looks like a title (all caps or long enough)
    lines = text.split("\n")
    for line in lines[:20]:
        line = line.strip()
        if not line or line.startswith("---"):
            continue
        # Skip very short lines (page numbers, dates)
        if len(line) < 10:
            continue
        meta["title"] = line
        break

    # Author / firm — look for "Prepared by:" or "By:" patterns
    for pattern in [
        r"[Pp]repared\s+[Bb]y[:\s]+(.+)",
        r"[Ss]ubmitted\s+[Bb]y[:\s]+(.+)",
        r"[Aa]uthor[:\s]+(.+)",
    ]:
        match = re.search(pattern, text[:3000])
        if match:
            meta["author"] = match.group(1).strip()
            break

    # Date — look for common date patterns
    for pattern in [
        r"[Dd]ate[:\s]+([A-Z][a-z]+\s+\d{1,2},?\s+\d{4})",
        r"([A-Z][a-z]+\s+\d{4})",
        r"(\d{1,2}/\d{1,2}/\d{4})",
    ]:
        match = re.search(pattern, text[:3000])
        if match:
            meta["date"] = match.group(1).strip()
            break

    return meta


# ---------------------------------------------------------------------------
# Document chunking
# ---------------------------------------------------------------------------

def _split_table_and_narrative(text: str) -> list[tuple[str, str]]:
    """Split text into alternating (type, content) segments.

    Returns list of ("narrative", text) and ("table", text) tuples.
    """
    segments: list[tuple[str, str]] = []
    parts = re.split(r"(\[TABLE\].*?\[/TABLE\])", text, flags=re.DOTALL)

    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith("[TABLE]") and part.endswith("[/TABLE]"):
            # Strip markers
            table_content = part[7:-8].strip()
            segments.append(("table", table_content))
        else:
            segments.append(("narrative", part))

    return segments


def _chunk_narrative_by_tokens(
    text: str,
    max_tokens: int,
    overlap_tokens: int,
) -> list[str]:
    """Split narrative text into token-sized chunks at sentence boundaries."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if not sentences:
        return [text] if text.strip() else []

    chunks: list[str] = []
    current_sents: list[str] = []
    current_tokens = 0

    for sent in sentences:
        sent_tokens = _count_tokens(sent)

        if current_tokens + sent_tokens > max_tokens and current_sents:
            # Emit current chunk
            chunks.append(" ".join(current_sents))

            # Keep overlap worth of sentences
            overlap_sents: list[str] = []
            overlap_count = 0
            for s in reversed(current_sents):
                s_tokens = _count_tokens(s)
                if overlap_count + s_tokens > overlap_tokens:
                    break
                overlap_sents.insert(0, s)
                overlap_count += s_tokens

            current_sents = overlap_sents
            current_tokens = overlap_count

        current_sents.append(sent)
        current_tokens += sent_tokens

    if current_sents:
        chunks.append(" ".join(current_sents))

    return chunks


def chunk_document(
    text: str,
    doc_meta: dict,
    package_id: str,
    *,
    max_tokens: int = 512,
    overlap_tokens: int = 50,
    tags: list[str] | None = None,
    is_csv: bool = False,
) -> list[Chunk]:
    """Chunk a document's text into Chunk objects for embedding.

    - Tables -> single chunks (chunk_type="table") regardless of token count
    - Narrative -> token-based chunking at sentence boundaries
    - CSV files -> single chunk (chunk_type="csv_data")

    Args:
        text: Full document text.
        doc_meta: Metadata dict from extract_doc_metadata().
        package_id: Package namespace (e.g., "project:juniper-canyon-dam").
        max_tokens: Target max tokens per narrative chunk.
        overlap_tokens: Token overlap between consecutive narrative chunks.
        tags: Optional tags to attach to all chunks.
        is_csv: If True, treat entire text as a single CSV data chunk.

    Returns:
        List of Chunk objects.
    """
    filename = doc_meta.get("filename", "unknown")
    title = doc_meta.get("title", filename)
    chunk_tags = tags or []
    chunks: list[Chunk] = []
    chunk_idx = 0

    if is_csv:
        chunk_id = f"{package_id}.{_slugify(filename)}.csv"
        chunks.append(Chunk(
            id=chunk_id,
            package_id=package_id,
            chunk_type="csv_data",
            title=title,
            content=text,
            metadata=doc_meta,
            tags=chunk_tags,
        ))
        return chunks

    # Split into table and narrative segments
    segments = _split_table_and_narrative(text)

    for seg_type, seg_text in segments:
        if seg_type == "table":
            chunk_id = f"{package_id}.{_slugify(filename)}.tbl-{chunk_idx}"
            chunks.append(Chunk(
                id=chunk_id,
                package_id=package_id,
                chunk_type="table",
                title=f"{title} (Table)",
                content=seg_text,
                metadata=doc_meta,
                tags=chunk_tags,
            ))
            chunk_idx += 1
        else:
            # Narrative — token-based chunking
            sub_chunks = _chunk_narrative_by_tokens(
                seg_text, max_tokens, overlap_tokens,
            )
            for sub_text in sub_chunks:
                chunk_id = f"{package_id}.{_slugify(filename)}.{chunk_idx}"
                chunks.append(Chunk(
                    id=chunk_id,
                    package_id=package_id,
                    chunk_type="narrative",
                    title=title,
                    content=sub_text,
                    metadata=doc_meta,
                    tags=chunk_tags,
                ))
                chunk_idx += 1

    return chunks


def _slugify(text: str) -> str:
    """Convert text to a URL-safe slug."""
    text = text.lower().strip()
    # Remove file extension
    text = re.sub(r"\.[a-z]+$", "", text)
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text.strip("-")
