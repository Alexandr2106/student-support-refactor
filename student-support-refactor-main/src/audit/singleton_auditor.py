import threading
from datetime import datetime
from typing import List, Dict

class AuditLoggerSingleton:
    _instance = None
    _lock = threading.Lock()
    _entries: List[Dict] = []

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, student_id: str, recipient: str, channel: str, result: str):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "student_id": student_id,
            "recipient": recipient,
            "channel": channel,
            "result": result
        }
        self._entries.append(entry)

    def get_logs(self) -> List[Dict]:
        return self._entries.copy()

    @classmethod
    def reset_for_test(cls):
        cls._entries.clear()
