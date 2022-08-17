# validation user's input
from pydantic import BaseModel, validator, Field, constr
from datetime import date
from typing import List


class Genre(BaseModel):
    name: str

class Autor(BaseModel):
    first_name: str = Field(..., max_length=25, min_length=1)
    last_name: str = Field(..., max_length=50, min_length=1)
    age:  int = Field(..., gt=15, lt=110, description="More 15, less 110")
    # @validator("age")
    # def check_age(cls, v):
    #     if v < 15:
    #         raise ValueError("Autor age must be more than 15")
    #     elif v >= 110:
    #         raise ValueError("Autor age must be less than 110")
    #     return v

class RandQuestionOut(BaseModel):
    id: str
    title: str = 'One random question'
    text: str
    cases: List[str] = []
    added_at: date = date.today()
    @validator("text")
    def check_len(cls, v):
        if len(v) > 300:
            raise ValueError("Text more than 300 characters")
        else:
            return v


class Book(BaseModel):
    title: str
    writer: str
    durations: str
    date: date
    summary: str
    genres: List[Genre] = []
    pages: int = 0

class BookOut(Book):
    id: int
