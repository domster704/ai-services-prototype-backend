from src.application.interfaces.language_detect_translate import (
    ILanguageDetectTranslate,
)
from src.application.interfaces.translate_multi_traduction import (
    ITranslateMultiTraduction,
)
from src.domain.language_detect_translate.entities import TranslatedAndDetectedObject
from src.domain.translate_multi_traduction.entities import TranslatedObject


class TranslatorHandler:
    def __init__(
        self,
        language_detect_translate: ILanguageDetectTranslate,
        translate_multi_traduction: ITranslateMultiTraduction,
    ):
        self.language_detect_translate = language_detect_translate
        self.translate_multi_traduction = translate_multi_traduction

    async def detect_and_translate(self, target, text: str) -> str:
        translated_object: TranslatedAndDetectedObject = (
            await self.language_detect_translate.translate(target, text=text)
        )

        return translated_object.translated

    async def translate(self, from_: str, to: str, q: str) -> str:
        translated_object: TranslatedObject = (
            await self.translate_multi_traduction.translate(from_, to, q)
        )

        return translated_object.translated
