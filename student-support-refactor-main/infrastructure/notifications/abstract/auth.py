# auth.py
class Authentication(ABC):
    @abstractmethod
    def get_token(self) -> str:
        pass
