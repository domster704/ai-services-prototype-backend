from typing import Protocol

from src.domain.text_gears.entities import (
    TextGearsTextToCheck,
)
from src.domain.trinka_grammar_checker.entities import TrinkaCheckResult


class ITextGears(Protocol):
    """
    TextGears (https://rapidapi.com/Textgears/api/textgears)
    AI-empowered spelling and grammar checker with automatic correction. Custom dictionaries, text summarization and keyword extraction. Language detection and readability calculator


    API с RapidAPI для проверки грамматики и орфографии
    """

    async def grammar_check(
        self, text_to_check: TextGearsTextToCheck
    ) -> TrinkaCheckResult:
        """
        Проверяет текст с помощью API TextGears (/grammar)

        Args:
            text_to_check (TextGearsTextToCheck): объект с текстом и языком для проверки грамматики

        Returns:
            TrinkaCheckResult: объект с результатом проверки и списком ошибок

        Raises:
            InfrastructureError: если произошла ошибка при обращении к API или при обработке ответа
            RapidApiError: если API вернул ошибку
        """
        ...
