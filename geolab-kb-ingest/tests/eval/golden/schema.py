"""Pydantic models for the KB RAG evaluation golden dataset."""

from __future__ import annotations

from pydantic import BaseModel, Field


class EvalQuestion(BaseModel):
    """A single ground-truth question with expected retrieval targets."""

    id: str = Field(..., description="e.g. Q001")
    question: str
    category: str = Field(
        ...,
        description=(
            "factual_lookup | numerical_data | table_query | cross_document | "
            "temporal | technical_detail | instrumentation | safety | "
            "geotechnical | procedural"
        ),
    )
    difficulty: str = Field(..., description="easy | medium | hard")
    source_doc: str = Field(..., description="Originating PDF filename")
    expected_chunk_ids: list[str] = Field(
        default_factory=list,
        description="All chunk IDs that contain the answer",
    )
    expected_chunk_id_primary: str = Field(
        ..., description="The single best chunk ID for this question"
    )
    acceptable_primary_ids: list[str] = Field(
        default_factory=list,
        description=(
            "Additional chunk IDs that are acceptable at rank 1. "
            "Any of these OR expected_chunk_id_primary at rank 1 counts as a P@1 hit."
        ),
    )
    expected_answer: str = Field(
        ..., description="Human-written reference answer"
    )
    answer_keywords: list[str] = Field(
        default_factory=list,
        description="Keywords that must appear in a correct answer",
    )
    expected_top_k: int = Field(
        default=5, description="Top-k to retrieve for this question"
    )
    min_acceptable_rank: int = Field(
        default=3,
        description="Primary chunk must appear within this rank to pass",
    )
    tags: list[str] = Field(
        default_factory=list, description="Topical tags for filtering"
    )


class EvalDataset(BaseModel):
    """The full golden evaluation dataset."""

    version: str = "1.0"
    project: str = "Juniper Canyon Dam"
    package_id: str = "project:juniper-canyon-dam"
    questions: list[EvalQuestion] = Field(default_factory=list)


class RetrievalResult(BaseModel):
    """Result of evaluating one question against the retrieval pipeline."""

    question_id: str
    question: str
    category: str
    difficulty: str
    expected_primary_chunk: str
    actual_chunks: list[RetrievedChunk] = Field(default_factory=list)
    primary_chunk_rank: int | None = Field(
        None, description="1-based rank of primary chunk, None if not found"
    )
    primary_chunk_score: float | None = Field(
        None, description="Cosine similarity of primary chunk"
    )
    passed: bool = False
    error: str | None = None


class RetrievedChunk(BaseModel):
    """A single chunk returned by the retrieval pipeline."""

    rank: int
    chunk_id: str
    title: str
    score: float


# Fix forward reference (RetrievedChunk used before definition in RetrievalResult)
RetrievalResult.model_rebuild()


class EvalReport(BaseModel):
    """Aggregate metrics from an evaluation run."""

    total_questions: int = 0
    recall_at_k: float = Field(0.0, description="% primary chunk in top-k")
    precision_at_1: float = Field(0.0, description="% primary chunk is rank 1")
    mrr: float = Field(0.0, description="Mean Reciprocal Rank")
    mean_cosine_similarity: float = Field(
        0.0, description="Mean cosine sim of primary chunks"
    )
    pass_rate: float = Field(
        0.0, description="% within min_acceptable_rank"
    )
    by_category: dict[str, CategoryMetrics] = Field(default_factory=dict)
    by_difficulty: dict[str, CategoryMetrics] = Field(default_factory=dict)
    results: list[RetrievalResult] = Field(default_factory=list)


class CategoryMetrics(BaseModel):
    """Metrics for a single category or difficulty slice."""

    count: int = 0
    recall_at_k: float = 0.0
    precision_at_1: float = 0.0
    mrr: float = 0.0
    pass_rate: float = 0.0


# Fix forward reference
EvalReport.model_rebuild()
