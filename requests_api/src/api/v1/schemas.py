from pydantic import BaseModel


class ModelIn(BaseModel):
    text: str
