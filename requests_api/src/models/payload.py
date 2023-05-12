from datetime import datetime

from pydantic import BaseModel


class Payload(BaseModel):
    user_id: str
    text: str
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: str
        }
