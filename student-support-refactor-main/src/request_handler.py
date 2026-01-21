from abc import ABC, abstractmethod
from .request_source import IRequestSource

# === Контракты уведомлений и логирования (остались без изменений) ===
class INotifier(ABC):
    @abstractmethod
    def send(self, student_id: str, message: str) -> None:
        pass

class IAuditLogger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# === Обработчик — получает зависимости извне ===
class RequestHandler:
    def __init__(
        self,
        request_source: IRequestSource,  # ← внедрение через конструктор
        notifier: INotifier,
        logger: IAuditLogger
    ):
        self._source = request_source
        self._notifier = notifier
        self._logger = logger

    def process(self, student_id: str, topic: str, text: str, channel: str, urgent_flag: bool) -> str:
        if not student_id or not topic.strip() or not text.strip():
            raise ValueError("Bad request")

        if urgent_flag:
            self._logger.log(f"URGENT: {student_id}")

        if self._source.exists(student_id, topic):
            self._logger.log(f"Duplicate request: {student_id}")
            return "Already exists"

        request_id = self._source.save(student_id, topic, text)
        self._notifier.send(student_id, f"Created request #{request_id}")
        self._logger.log(f"Created request id={request_id}")

        if "password" in topic.lower():
            return "Reset instruction sent"
        elif "schedule" in topic.lower():
            return "We will check schedule"
        else:
            return "Request accepted"
