from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle(self, *args, **kwargs):
        raise NotImplementedError
