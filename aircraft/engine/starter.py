from abc import ABC, abstractmethod


class Engine(ABC):

    @abstractmethod
    def start(self, *args, **kwargs) -> None:
        ...

    def shutdown(self) -> None:
        ...
