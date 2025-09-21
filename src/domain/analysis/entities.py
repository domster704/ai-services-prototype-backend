from dataclasses import dataclass
from enum import Enum


class UnifiedErrorProvider(str, Enum):
    TRINKA = "trinka"
    TEXT_GEARS = "text_gears"


@dataclass(eq=True, frozen=True)
class UnifiedError:
    offset: int
    length: int
    covered_text: str
    suggestions: list[str]
    comment: str | None
    category: str
    provider: UnifiedErrorProvider


@dataclass(eq=True, frozen=True)
class UnifiedErrorComparison:
    common: list[UnifiedError]
    only_text_gears: list[UnifiedError]
    only_trinka: list[UnifiedError]
