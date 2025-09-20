from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.presentation.api.v1.language_detect_translate import (
    router_language_detect_translate,
)
from src.presentation.api.v1.translate_multi_traduction import (
    router_translate_multi_traduction,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="ERS_Lab_1", lifespan=lifespan)
app.include_router(router_language_detect_translate, prefix="/v1")
app.include_router(
    router_translate_multi_traduction,
    prefix="/v1",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
