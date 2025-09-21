from pydantic import BaseModel


class TextGearsGrammarCheckerErrorDTO(BaseModel):
    bad: str
    better: list[str]
    description: dict[str, str]
    id: str
    length: int
    offset: int
    type: str


class TextGearsGrammarCheckerResponseDTO(BaseModel):
    result: bool
    errors: list[TextGearsGrammarCheckerErrorDTO]


class TextGearsGrammarCheckerObjectDTO(BaseModel):
    status: bool
    response: TextGearsGrammarCheckerResponseDTO
