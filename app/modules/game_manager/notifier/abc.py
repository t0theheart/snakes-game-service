from abc import ABC, abstractmethod


class NotifierABC(ABC):
    @abstractmethod
    async def notify(self, *args, **kwargs):
        pass
