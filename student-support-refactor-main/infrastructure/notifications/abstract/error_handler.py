# error_handler.py
class ErrorHandler(ABC):
    @abstractmethod
    def handle(self, error: Exception) -> None:
        pass
