from pydantic import BaseModel


class TrinkaResultDTO(BaseModel):
    # start_index: int
    # end_index: int
    covered_text: str
    output: list[str]
    comment: list[str]
    # cta_present: list[bool]
    error_category: list[str]


class TrinkaItemDTO(BaseModel):
    # begin: int
    # end: int
    sentence: str
    result: list[TrinkaResultDTO]


class TrinkaCheckResultDTO(BaseModel):
    sentences: list[TrinkaItemDTO]
