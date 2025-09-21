from dataclasses import dataclass

SUPPORTED_LANGUAGES: set[str] = {
    "en",  # English
    "es",  # Spanish
    "de",  # German
}


@dataclass(eq=True, frozen=True)
class TrinkaTextToCheck:
    paragraph: str
    language: str

    def __post_init__(self) -> None:
        """
        Проверяет корректность данных для правильной работы с API
        """

        if self.language not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Неподдерживаемый язык: {self.language}.\nДолжен быть одним из {', '.join(SUPPORTED_LANGUAGES)}"
            )


@dataclass(eq=True, frozen=True)
class TrinkaResult:
    start_index: int
    end_index: int
    covered_text: str
    output: list[str]
    comment: list[str]
    cta_present: list[bool]
    error_category: list[str]


@dataclass(eq=True, frozen=True)
class TrinkaItem:
    begin: int
    end: int
    sentence: str
    result: list[TrinkaResult]


@dataclass(eq=True, frozen=True)
class TrinkaCheckResult:
    sentences: list[TrinkaItem]
