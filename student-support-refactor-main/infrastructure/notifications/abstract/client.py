# client.py
from abc import ABC, abstractmethod

class MessengerClient(ABC):
    @abstractmethod
    def send(self, message: str) -> bool:
        pass
