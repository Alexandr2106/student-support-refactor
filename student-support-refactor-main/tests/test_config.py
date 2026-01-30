import pytest
from src.config.singleton_config import AppConfigSingleton
from src.config.di_config import AppConfig

def test_singleton_is_unique():
    a = AppConfigSingleton()
    b = AppConfigSingleton()
    assert a is b

def test_singleton_reset():
    AppConfigSingleton.reset_for_test()
    a = AppConfigSingleton()
    b = AppConfigSingleton()
    assert a is b

def test_di_config_independent():
    cfg1 = AppConfig("config.yaml")
    cfg2 = AppConfig("config.yaml")
    assert cfg1 is not cfg2
    assert cfg1.get("dataSourceType") == cfg2.get("dataSourceType")
