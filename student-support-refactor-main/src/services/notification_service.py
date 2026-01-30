from src.audit.di_auditor import AuditLogger
from src.config.di_config import AppConfig
from src.integration.messenger_client import IMessengerClient

class NotificationService:
    def __init__(
        self,
        messenger: IMessengerClient,
        config: AppConfig,
        auditor: AuditLogger
    ):
        self.messenger = messenger
        self.config = config
        self.auditor = auditor

    def send_notification(self, student_id: str, message: str, recipient: str):
        channel = self.config.get("notification_channel", "email")
        try:
            self.messenger.send(student_id, message)
            self.auditor.log(student_id, recipient, channel, "success")
        except Exception as e:
            self.auditor.log(student_id, recipient, channel, f"error: {e}")
            raise
