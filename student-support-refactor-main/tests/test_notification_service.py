from unittest.mock import Mock
from src.services.notification_service import NotificationService
from src.config.di_config import AppConfig
from src.audit.di_auditor import AuditLogger

def test_service_with_di():
    mock_messenger = Mock()
    config = AppConfig("config.yaml")
    auditor = AuditLogger()

    svc = NotificationService(mock_messenger, config, auditor)
    svc.send_notification("123", "Hello", "admin")

    mock_messenger.send.assert_called_once_with("123", "Hello")
    logs = auditor.get_logs()
    assert len(logs) == 1
    assert logs[0]["result"] == "success"
