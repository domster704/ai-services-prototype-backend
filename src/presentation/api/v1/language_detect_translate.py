from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from src.application.translator.handlers import TranslatorHandler
from src.infrastructure.depends import get_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError

router_language_detect_translate = APIRouter(
    prefix="/language_detect_translate",
    tags=["Language Detect & Translate"],
)


class TranslateBody(BaseModel):
    target: str
    text: str


@router_language_detect_translate.post("/translate", status_code=200)
async def translate(
    body: TranslateBody, handler: TranslatorHandler = Depends(get_handler)
) -> dict[str, str]:
    try:
        translated_text = await handler.detect_and_translate(
            target=body.target, text=body.text
        )

        return {"message": translated_text}
    except InfrastructureError as e:
        print(e)
        raise HTTPException(status_code=503, detail=f"Infrastructure error: {str(e)}")
    except RapidApiError as e:
        print(e)
        raise HTTPException(status_code=502, detail=f"RapidAPI error: {str(e)}")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
