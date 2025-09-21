from pydantic import BaseModel

from src.domain.analysis.entities import UnifiedError, UnifiedErrorComparison


class UnifiedErrorDTO(BaseModel):
    offset: int
    length: int
    covered_text: str
    suggestions: list[str]
    comment: str | None
    category: str
    provider: str


class ComparisonResultDTO(BaseModel):
    common: list[UnifiedErrorDTO]
    only_text_gears: list[UnifiedErrorDTO]
    only_trinka: list[UnifiedErrorDTO]
