from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.presentation.api.v1.grammar_checker.analysis.router import (
    router_grammar_checker_analysis,
)
from src.presentation.api.v1.grammar_checker.text_gears.router import router_text_gears
from src.presentation.api.v1.grammar_checker.trinka_grammar_checker.router import (
    router_trinka_grammar_checker,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="ERS_Lab_1",
    lifespan=lifespan,
    description="""
API для проверки грамматики через два сервиса:
- TextGears
- Trinka Grammar Checker

Поддерживает:
- Грамматическую проверку текста отдельно через каждый сервис
- Унифицированное сравнение ошибок грамматики
""",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_text_gears, prefix="/v1")
app.include_router(router_trinka_grammar_checker, prefix="/v1")
app.include_router(router_grammar_checker_analysis, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
