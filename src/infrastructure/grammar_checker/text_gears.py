import aiohttp

from src.application.interfaces.text_gears import ITextGears
from src.config.settings import settings
from src.domain.text_gears.entities import (
    TextGearsGrammarCheckerObject,
    TextGearsTextToCheck,
)
from src.infrastructure.exceptions import InfrastructureError, RapidApiError


class TextGearsRapidApi(ITextGears):
    async def grammar_check(
        self, text_to_check: TextGearsTextToCheck
    ) -> TextGearsGrammarCheckerObject:
        try:
            async with aiohttp.ClientSession(
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "x-rapidapi-host": "textgears-textgears-v1.p.rapidapi.com",
                    "x-rapidapi-key": settings.rapid_api_key,
                }
            ) as session:
                form_data = aiohttp.FormData()
                form_data.add_field("text", text_to_check.text)
                form_data.add_field("language", text_to_check.language)

                async with session.post(
                    "https://textgears-textgears-v1.p.rapidapi.com/grammar",
                    proxy=settings.proxy_url,
                    data=form_data,
                ) as resp:
                    if not resp.ok:
                        raise RapidApiError(
                            f"Запрос не удался. Код ответа: {resp.status}. Текст ошибки: {resp.text}"
                        )
                    data = await resp.json()
                    return TextGearsGrammarCheckerObject(**data)
        except aiohttp.ClientError as e:
            raise InfrastructureError(e)
