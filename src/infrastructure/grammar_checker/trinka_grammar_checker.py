import aiohttp
from dacite import from_dict

from src.application.interfaces.trinka_grammar_checker import ITrinkaGrammarChecker
from src.config.settings import settings
from src.domain.trinka_grammar_checker.entities import (
    TrinkaCheckResult,
    TrinkaTextToCheck,
    TrinkaItem,
)
from src.infrastructure.exceptions import InfrastructureError, RapidApiError


class TrinkaGrammarCheckerRapidApi(ITrinkaGrammarChecker):
    async def grammar_check(
        self, text_to_check: TrinkaTextToCheck
    ) -> TrinkaCheckResult:
        try:
            async with aiohttp.ClientSession(
                headers={
                    "Content-Type": "application/json",
                    "x-rapidapi-host": "trinka-grammar-checker.p.rapidapi.com",
                    "x-rapidapi-key": settings.rapid_api_key,
                }
            ) as session:
                async with session.post(
                    f"https://trinka-grammar-checker.p.rapidapi.com/v2/para-check/{text_to_check.language}",
                    proxy=settings.proxy_url,
                    json={
                        "paragraph": text_to_check.paragraph,
                    },
                ) as resp:
                    if not resp.ok:
                        raise RapidApiError(
                            f"Запрос не удался. Код ответа: {resp.status}. Текст ошибки: {resp.text}"
                        )
                    data: list[TrinkaItem] = await resp.json()
                    return from_dict(
                        data_class=TrinkaCheckResult, data={"sentences": data}
                    )
        except aiohttp.ClientError as e:
            raise InfrastructureError(e)
