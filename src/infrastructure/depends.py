from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.application.interfaces.language_detect_translate import (
    ILanguageDetectTranslate,
)
from src.application.interfaces.translate_multi_traduction import (
    ITranslateMultiTraduction,
)
from src.application.translator.handlers import TranslatorHandler
from src.infrastructure.grammar_checker.text_gears import TextGearsRapidApi
from src.infrastructure.translator.language_detect_translate import (
    LanguageDetectTranslateRapidApi,
)
from src.infrastructure.translator.translate_multi_traduction import (
    TranslateMultiTraductionRapidApi,
)


def get_handler():
    language_detect_translate: ILanguageDetectTranslate = (
        LanguageDetectTranslateRapidApi()
    )
    translate_multi_traduction: ITranslateMultiTraduction = (
        TranslateMultiTraductionRapidApi()
    )
    handler = TranslatorHandler(
        language_detect_translate=language_detect_translate,
        translate_multi_traduction=translate_multi_traduction,
    )
    return handler


def get_grammar_checker_handler() -> GrammarCheckerHandler:
    text_gears: TextGearsRapidApi = TextGearsRapidApi()

    handler = GrammarCheckerHandler(text_gears=text_gears)
    return handler
