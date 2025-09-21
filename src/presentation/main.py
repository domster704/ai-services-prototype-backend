from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.presentation.api.v1.text_gears.text_gears import router_text_gears


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="ERS_Lab_1", lifespan=lifespan)
app.include_router(router_text_gears, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
