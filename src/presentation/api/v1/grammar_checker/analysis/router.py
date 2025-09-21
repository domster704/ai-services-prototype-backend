import traceback
from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.application.grammar_checker.language_mapping import to_textgears, to_trinka
from src.infrastructure.depends import get_grammar_checker_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError
from src.presentation.api.v1.grammar_checker.analysis.dto import (
    ComparisonResultDTO,
)

router_grammar_checker_analysis = APIRouter(
    prefix="/grammar_checker_analysis",
    tags=["Grammar Checker Analysis"],
)


class GrammarCheckBody(BaseModel):
    text: str
    language: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Exmaple text with errrosr",
                    "language": "en",
                }
            ]
        }
    }


@router_grammar_checker_analysis.post(
    "/grammar",
    status_code=200,
    summary="Унифицированная проверка текста",
    description="""
Выполняет проверку текста сразу в двух сервисах: TextGears и Trinka.
Возвращает:
- ошибки, найденные обоими сервисами
- уникальные ошибки каждого из них
""",
)
async def translate(
    body: GrammarCheckBody,
    handler: GrammarCheckerHandler = Depends(get_grammar_checker_handler),
) -> ComparisonResultDTO:
    try:
        tg_lang = to_textgears(body.language)
        trinka_lang = to_trinka(body.language)

        tg_result = await handler.grammar_check_text_gears(body.text, tg_lang)
        trinka_result = await handler.grammar_check_trinka(body.text, trinka_lang)

        comparison = handler.unified_analyze(tg_result, trinka_result)

        return ComparisonResultDTO.model_validate(asdict(comparison))
    except InfrastructureError as e:
        print(e)
        raise HTTPException(status_code=503, detail=f"InfrastructureError: {str(e)}")
    except RapidApiError as e:
        print(e)
        raise HTTPException(status_code=502, detail=f"RapidApiError: {str(e)}")
    except ValueError as e:
        print(e)
        raise HTTPException(status_code=400, detail=f"ValueError: {str(e)}")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"InternalError: {str(e)}")
