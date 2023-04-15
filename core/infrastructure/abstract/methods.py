from abc import ABC, abstractmethod
from typing import Optional


class Executor(ABC):

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> any:

        ...


class Engine(ABC):

    @abstractmethod
    def start(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def shutdown(self) -> None:
        ...
