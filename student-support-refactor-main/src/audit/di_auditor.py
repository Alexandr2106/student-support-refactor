from datetime import datetime
from typing import List, Dict

class AuditLogger:
    def __init__(self):
        self._entries: List[Dict] = []

    def log(self, student_id: str, recipient: str, channel: str, result: str):
        self._entries.append({
            "timestamp": datetime.now().isoformat(),
            "student_id": student_id,
            "recipient": recipient,
            "channel": channel,
            "result": result
        })

    def get_logs(self) -> List[Dict]:
        return self._entries.copy()
