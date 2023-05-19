from functools import lru_cache

from lib.base import BaseModel


class RequestClassifierService(BaseModel):
    def __init__(self):
        self.classifier = None  # TODO сюда вставить код загрузки модели

    def compute(self, text: str) -> str:
        pass  # TODO Здесь код классификации


@lru_cache
def get_request_classifier_service() -> RequestClassifierService:
    return RequestClassifierService()
