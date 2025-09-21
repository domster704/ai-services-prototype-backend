from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.infrastructure.grammar_checker.text_gears import TextGearsRapidApi
from src.infrastructure.grammar_checker.trinka_grammar_checker import (
    TrinkaGrammarCheckerRapidApi,
)


def get_grammar_checker_handler() -> GrammarCheckerHandler:
    text_gears: TextGearsRapidApi = TextGearsRapidApi()
    trinka_grammar_checker: TrinkaGrammarCheckerRapidApi = (
        TrinkaGrammarCheckerRapidApi()
    )

    handler = GrammarCheckerHandler(
        text_gears=text_gears, trinka_grammar_checker=trinka_grammar_checker
    )
    return handler
