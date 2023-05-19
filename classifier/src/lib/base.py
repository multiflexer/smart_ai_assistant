from typing import Any
from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def compute(self, *args, **kwargs) -> Any:
        pass
