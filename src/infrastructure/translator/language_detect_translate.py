import aiohttp

from src.application.interfaces.language_detect_translate import (
    ILanguageDetectTranslate,
)
from src.config.settings import settings
from src.domain.language_detect_translate.entities import TranslatedAndDetectedObject
from src.infrastructure.exceptions import InfrastructureError, RapidApiError


class LanguageDetectTranslateRapidApi(ILanguageDetectTranslate):
    async def translate(self, target: str, text: str) -> TranslatedAndDetectedObject:
        try:
            async with aiohttp.ClientSession(
                headers={
                    "Content-Type": "application/json",
                    "x-rapidapi-host": "language-detect-translate.p.rapidapi.com",
                    "x-rapidapi-key": settings.rapid_api_key,
                }
            ) as session:
                async with session.post(
                    "https://language-detect-translate.p.rapidapi.com/detect-translate",
                    proxy="http://127.0.0.1:12334",
                    json={"target": target, "text": text},
                ) as resp:
                    if not resp.ok:
                        raise RapidApiError(
                            f"Request failed with status code {resp.status}"
                        )
                    data = await resp.json()
                    return TranslatedAndDetectedObject(**data)
        except aiohttp.ClientError as e:
            raise InfrastructureError(e)
