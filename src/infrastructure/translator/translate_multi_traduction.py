import aiohttp

from src.application.interfaces.translate_multi_traduction import (
    ITranslateMultiTraduction,
)
from src.config.settings import settings
from src.domain.translate_multi_traduction.entities import TranslatedObject
from src.infrastructure.exceptions import InfrastructureError, RapidApiError


class TranslateMultiTraductionRapidApi(ITranslateMultiTraduction):
    async def translate(self, from_: str, to: str, q: str) -> TranslatedObject:
        try:
            async with aiohttp.ClientSession(
                headers={
                    "Content-Type": "application/json",
                    "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
                    "x-rapidapi-key": settings.rapid_api_key,
                }
            ) as session:
                async with session.post(
                    "https://rapid-translate-multi-traduction.p.rapidapi.com/t",
                    proxy="http://127.0.0.1:12334",
                    json={"from": from_, "to": to, "q": q},
                ) as resp:
                    if not resp.ok:
                        raise RapidApiError(
                            f"Request failed with status code {resp.status}"
                        )
                    data: list[str] = await resp.json()

                    return TranslatedObject.from_list(data)
        except aiohttp.ClientError as e:
            raise InfrastructureError(e)
