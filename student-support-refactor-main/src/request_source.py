from abc import ABC, abstractmethod
import uuid

# === Контракт ===
class IRequestSource(ABC):
    @abstractmethod
    def exists(self, student_id: str, topic: str) -> bool:
        pass

    @abstractmethod
    def save(self, student_id: str, topic: str, text: str) -> str:
        pass


# === Реализация: База данных (имитация) ===
class DatabaseRequestSource(IRequestSource):
    def __init__(self):
        # В реальности: подключение к БД
        self._storage = {}

    def exists(self, student_id: str, topic: str) -> bool:
        return (student_id, topic) in self._storage

    def save(self, student_id: str, topic: str, text: str) -> str:
        req_id = f"DB-{uuid.uuid4().hex[:8]}"
        self._storage[(student_id, topic)] = {"id": req_id, "text": text}
        return req_id


# === Реализация: Файл (в памяти) ===
class FileRequestSource(IRequestSource):
    def __init__(self):
        self._storage = {}

    def exists(self, student_id: str, topic: str) -> bool:
        return (student_id, topic) in self._storage

    def save(self, student_id: str, topic: str, text: str) -> str:
        req_id = f"FILE-{uuid.uuid4().hex[:8]}"
        self._storage[(student_id, topic)] = {"id": req_id, "text": text}
        return req_id


# === Реализация: Веб-сервис (имитация) ===
class WebServiceRequestSource(IRequestSource):
    def __init__(self):
        self._storage = {}

    def exists(self, student_id: str, topic: str) -> bool:
        return (student_id, topic) in self._storage

    def save(self, student_id: str, topic: str, text: str) -> str:
        req_id = f"WEB-{uuid.uuid4().hex[:8]}"
        self._storage[(student_id, topic)] = {"id": req_id, "text": text}
        return req_id
