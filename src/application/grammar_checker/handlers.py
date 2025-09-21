from src.application.interfaces.text_gears import ITextGears
from src.domain.text_gears.entities import TextToCheck, TextGearsGrammarCheckerObject


class GrammarCheckerHandler:
    def __init__(
        self,
        text_gears: ITextGears,
    ):
        self.text_gears = text_gears

    async def grammar_check_text_gears(
        self, text: str, language: str
    ) -> TextGearsGrammarCheckerObject:
        text_to_check = TextToCheck(text=text, language=language)

        grammar_checked_object: TextGearsGrammarCheckerObject = (
            await self.text_gears.grammar_check(text_to_check)
        )

        return grammar_checked_object
