from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.application.grammar_checker.handlers import GrammarCheckerHandler
from src.infrastructure.depends import get_grammar_checker_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError
from src.presentation.api.v1.text_gears.dto import TextGearsGrammarCheckerObjectDTO

router_text_gears = APIRouter(
    prefix="/text_gears",
    tags=["TextGears"],
)


class GrammarCheckBody(BaseModel):
    text: str
    language: str


@router_text_gears.post("/grammar", status_code=200)
async def translate(
    body: GrammarCheckBody,
    handler: GrammarCheckerHandler = Depends(get_grammar_checker_handler),
) -> TextGearsGrammarCheckerObjectDTO:
    try:
        grammar_checked_object = await handler.grammar_check_text_gears(
            text=body.text, language=body.language
        )

        return TextGearsGrammarCheckerObjectDTO.model_validate(
            grammar_checked_object.__dict__
        )
    except InfrastructureError as e:
        print(e)
        raise HTTPException(status_code=503, detail=f"InfrastructureError: {str(e)}")
    except RapidApiError as e:
        print(e)
        raise HTTPException(status_code=502, detail=f"RapidApiError: {str(e)}")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"InternalError: {str(e)}")
