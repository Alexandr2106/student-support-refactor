import pytest
from unittest.mock import Mock
from src.request_handler import RequestHandler

# Имитация источника данных для тестов
class FakeRequestSource:
    def __init__(self, exists_result=False, save_id="TEST-123"):
        self._exists_result = exists_result
        self._save_id = save_id
        self.saved = []

    def exists(self, student_id, topic):
        return self._exists_result

    def save(self, student_id, topic, text):
        self.saved.append((student_id, topic, text))
        return self._save_id


def test_process_new_request():
    source = FakeRequestSource(exists_result=False, save_id="REQ-999")
    notifier = Mock()
    logger = Mock()

    handler = RequestHandler(source, notifier, logger)

    result = handler.process("S123", "schedule", "When is exam?", "email", False)

    assert result == "We will check schedule"
    assert len(source.saved) == 1
    notifier.send.assert_called_once_with("S123", "Created request #REQ-999")


def test_process_duplicate_request():
    source = FakeRequestSource(exists_result=True)
    notifier = Mock()
    logger = Mock()

    handler = RequestHandler(source, notifier, logger)

    result = handler.process("S123", "password", "Forgot password", "email", False)

    assert result == "Already exists"
    assert len(source.saved) == 0
    notifier.send.assert_not_called()


# Дополнительные тесты — проверка разных ID-форматов (необязательно, но хорошо)
def test_db_source_generates_id():
    from src.request_source import DatabaseRequestSource
    source = DatabaseRequestSource()
    rid = source.save("S1", "topic", "text")
    assert rid.startswith("DB-")
    assert len(rid) == 11  # DB- + 8 hex


def test_file_source_generates_id():
    from src.request_source import FileRequestSource
    source = FileRequestSource()
    rid = source.save("S1", "topic", "text")
    assert rid.startswith("FILE-")
