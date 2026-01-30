from src.audit.singleton_auditor import AuditLoggerSingleton
from src.audit.di_auditor import AuditLogger

def test_singleton_auditor_leak():
    AuditLoggerSingleton.reset_for_test()
    logger1 = AuditLoggerSingleton()
    logger1.log("s1", "t1", "email", "ok")
    
    logger2 = AuditLoggerSingleton()
    assert len(logger2.get_logs()) == 1

def test_di_auditor_isolated():
    logger1 = AuditLogger()
    logger1.log("s1", "t1", "email", "ok")
    
    logger2 = AuditLogger()
    assert len(logger2.get_logs()) == 0
