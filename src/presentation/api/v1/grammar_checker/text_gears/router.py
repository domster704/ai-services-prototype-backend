from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.infrastructure.depends import get_grammar_checker_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError
from src.presentation.api.v1.grammar_checker.text_gears.dto import (
    TextGearsGrammarCheckerObjectDTO,
)

router_text_gears = APIRouter(
    prefix="/text_gears",
    tags=["TextGears"],
)


class GrammarCheckBody(BaseModel):
    text: str
    language: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "text": "Exmaple text with errrosr",
                    "language": "en-US",
                }
            ]
        }
    }


@router_text_gears.post(
    "/grammar",
    status_code=200,
    summary="Грамматическая проверка текста через TextGears с помощью RapidAPI",
)
async def translate(
    body: GrammarCheckBody,
    handler: GrammarCheckerHandler = Depends(get_grammar_checker_handler),
) -> TextGearsGrammarCheckerObjectDTO:
    try:
        grammar_checked_object = await handler.grammar_check_text_gears(
            text=body.text, language=body.language
        )

        return TextGearsGrammarCheckerObjectDTO.model_validate(
            asdict(grammar_checked_object)
        )
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
        raise HTTPException(status_code=500, detail=f"InternalError: {str(e)}")
