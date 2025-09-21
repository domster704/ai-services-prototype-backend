from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.infrastructure.depends import get_grammar_checker_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError
from src.presentation.api.v1.grammar_checker.trinka_grammar_checker.dto import (
    TrinkaCheckResultDTO,
)

router_trinka_grammar_checker = APIRouter(
    prefix="/trinka_grammar_checker",
    tags=["Trinka Grammar Checker"],
)


class GrammarCheckBody(BaseModel):
    paragraph: str
    language: str


@router_trinka_grammar_checker.post("/grammar", status_code=200)
async def translate(
    body: GrammarCheckBody,
    handler: GrammarCheckerHandler = Depends(get_grammar_checker_handler),
) -> TrinkaCheckResultDTO:
    try:
        grammar_checked_object = await handler.grammar_check_trinka(
            text=body.paragraph, language=body.language
        )

        return TrinkaCheckResultDTO.model_validate(asdict(grammar_checked_object))
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
