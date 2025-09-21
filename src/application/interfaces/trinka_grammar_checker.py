from typing import Protocol

from src.domain.trinka_grammar_checker.entities import (
    TrinkaTextToCheck,
    TrinkaCheckResult,
)


class ITrinkaGrammarChecker(Protocol):
    """
    Trinka Grammar Checker (https://rapidapi.com/trinka-grammar-checker-api-trinka-grammar-checker-api-default/api/trinka-grammar-checker)
    Trinka’s Grammar and Spell Check API is an AI-powered language correction
    API. In addition to providing corrections of grammar and spelling errors,
    it also provides suggestions to enhance the language. The output of the
    API consists of errors annoated with language categories for ease of customization.

    API с RapidAPI для проверки грамматики и орфографии
    """

    async def grammar_check(
        self, text_to_check: TrinkaTextToCheck
    ) -> TrinkaCheckResult:
        """
        Проверяет текст с помощью API Trinka Grammar Checker (/para-check/en )

        Args:
            text_to_check (TrinkaTextToCheck): объект с текстом и языком для проверки грамматики

        Returns:
            TrinkaCheckResult: объект с результатом проверки и списком ошибок

        Raises:
            InfrastructureError: если произошла ошибка при обращении к API или при обработке ответа
            RapidApiError: если API вернул ошибку
        """
        ...
