from dataclasses import dataclass
from enum import Enum

SUPPORTED_LANGUAGES: set[str] = {
    "en-US",
    "en-GB",
    "en-ZA",
    "en-AU",
    "en-NZ",
    "fr-FR",
    "de-DE",
    "de-AT",
    "de-CH",
    "pt-PT",
    "pt-BR",
    "it-IT",
    "ar-AR",
    "ru-RU",
    "es-ES",
    "ja-JP",
    "zh-CN",
    "el-GR",
}

MAX_TEXT_GEARS_STR_LENGTH: int = 8192


@dataclass(eq=True, frozen=True)
class TextToCheck:
    text: str
    language: str

    def __post_init__(self) -> None:
        """
        Проверяет корректность данных для правильной работы с API
        """
        if len(self.text) > MAX_TEXT_GEARS_STR_LENGTH:
            raise ValueError("Длина текста не должна превышать 8192 символов")

        if self.language not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Неподдерживаемый язык: {self.language}.\nДолжен быть одним из {', '.join(SUPPORTED_LANGUAGES)}"
            )


class ErrorType(str, Enum):
    GRAMMAR = "grammar"
    SPELLING = "spelling"


@dataclass(eq=True, frozen=True)
class TextGearsGrammarCheckerError:
    bad: str
    better: list[str]
    description: dict[str, str]
    id: str
    length: int
    offset: int
    type: ErrorType


@dataclass(eq=True, frozen=True)
class TextGearsGrammarCheckerResponse:
    errors: list[TextGearsGrammarCheckerError]
    result: bool


@dataclass(eq=True, frozen=True)
class TextGearsGrammarCheckerObject:
    status: bool
    response: TextGearsGrammarCheckerResponse
