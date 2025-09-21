from src.application.interfaces.text_gears import ITextGears
from src.application.interfaces.trinka_grammar_checker import ITrinkaGrammarChecker
from src.domain.text_gears.entities import (
    TextGearsTextToCheck,
    TextGearsGrammarCheckerObject,
)
from src.domain.trinka_grammar_checker.entities import (
    TrinkaTextToCheck,
    TrinkaCheckResult,
)


class GrammarCheckerHandler:
    def __init__(
        self, text_gears: ITextGears, trinka_grammar_checker: ITrinkaGrammarChecker
    ):
        self.text_gears = text_gears
        self.trinka_grammar_checker = trinka_grammar_checker

    async def grammar_check_text_gears(
        self, text: str, language: str
    ) -> TextGearsGrammarCheckerObject:
        text_to_check = TextGearsTextToCheck(text=text, language=language)

        grammar_checked_object: TextGearsGrammarCheckerObject = (
            await self.text_gears.grammar_check(text_to_check)
        )

        return grammar_checked_object

    async def grammar_check_trinka(self, text: str, language: str) -> TrinkaCheckResult:
        text_to_check = TrinkaTextToCheck(paragraph=text, language=language)

        grammar_checked_object: TrinkaCheckResult = (
            await self.trinka_grammar_checker.grammar_check(text_to_check)
        )

        return grammar_checked_object
