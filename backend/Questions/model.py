# models.py
from pydantic import BaseModel

class Question(BaseModel):
    text: str

class Response(BaseModel):
    response: str