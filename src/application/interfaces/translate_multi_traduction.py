from typing import Protocol

from src.domain.translate_multi_traduction.entities import TranslatedObject


class ITranslateMultiTraduction(Protocol):
    """
    Rapid Translate Multi Traduction (https://rapidapi.com/sibaridev/api/rapid-translate-multi-traduction)

    API с RapidAPI, которое позволяет быстро переводить текст с одного языка на другой.
    """

    async def translate(self, from_: str, to: str, q: str) -> TranslatedObject:
        """
        Функция переводит текст с одного языка на другой
        Args:
            from_: строка из двух символов, обозначающих язык, с которого нужно перевести текст.
            to: строка из двух символов, обозначающих язык, на который нужно перевести текст.
            q: строка, которую нужно перевести.

        Returns:
            TranslatedObject: переведенный текст на целевой язык

        Raises:
            InfrastructureError: если произошла ошибка при обращении к API или при обработке ответа
            RapidApiError: если произошла ошибка при обращении к RapidAPI
        """
        ...
