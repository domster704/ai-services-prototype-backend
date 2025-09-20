from src.application.interfaces.language_detect_translate import (
    ILanguageDetectTranslate,
)
from src.application.interfaces.translate_multi_traduction import (
    ITranslateMultiTraduction,
)
from src.application.translator.handlers import TranslatorHandler
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
