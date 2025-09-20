from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from src.application.translator.handlers import TranslatorHandler
from src.infrastructure.depends import get_handler
from src.infrastructure.exceptions import InfrastructureError, RapidApiError

router_translate_multi_traduction = APIRouter(
    prefix="/translate_multi_traduction", tags=["Rapid Translate Multi Traduction"]
)


class TranslateBody(BaseModel):
    from_: str = Field(alias="from")
    to: str
    q: str


@router_translate_multi_traduction.post("/translate", status_code=200)
async def translate(
    body: TranslateBody, handler: TranslatorHandler = Depends(get_handler)
) -> dict[str, str]:
    try:
        translated_text = await handler.translate(
            from_=body.from_, to=body.to, q=body.q
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
