from typing import Protocol

from src.domain.language_detect_translate.entities import TranslatedAndDetectedObject


class ILanguageDetectTranslate(Protocol):
    """
    Language Detect & Translate (https://rapidapi.com/mohamedmouminchk/api/language-detect-translate)
    Instantly detect the language of any text and translate it to your target language in one simple API call. Fast, easy, and supports 100+ languages.


    API с RapidAPI, которое позволяет быстро определять язык текста и переводить его на целевой язык.
    """

    async def translate(self, target: str, text: str) -> TranslatedAndDetectedObject:
        """
        Функция переводит текст с одного языка на другой
        Args:
            target: строка из двух символов, обозначающих язык, на который нужно перевести текст.
            text: строка, которую нужно перевести.

        Returns:
            TranslatedAndDetectedObject: переведенный текст на целевой язык

        Raises:
            InfrastructureError: если произошла ошибка при обращении к API или при обработке ответа
            RapidApiError: если произошла ошибка при обращении к RapidAPI
        """
        ...
