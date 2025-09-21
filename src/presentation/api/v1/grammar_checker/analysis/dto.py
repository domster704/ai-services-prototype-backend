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


def to_dto_error(error: UnifiedError) -> UnifiedErrorDTO:
    return UnifiedErrorDTO(
        offset=error.offset,
        length=error.length,
        covered_text=error.covered_text,
        suggestions=error.suggestions,
        comment=error.comment,
        category=error.category,
        provider=(
            error.provider.value
            if hasattr(error.provider, "value")
            else str(error.provider)
        ),
    )


def to_dto_result(result: UnifiedErrorComparison) -> ComparisonResultDTO:
    return ComparisonResultDTO(
        common=[to_dto_error(e) for e in result.common],
        only_text_gears=[to_dto_error(e) for e in result.only_text_gears],
        only_trinka=[to_dto_error(e) for e in result.only_trinka],
    )
