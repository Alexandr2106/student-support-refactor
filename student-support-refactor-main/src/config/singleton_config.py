import threading
import yaml
from pathlib import Path
from typing import Any

class AppConfigSingleton:
    _instance = None
    _lock = threading.Lock()
    _loaded = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._loaded:
            self._load_from_file()
            self._loaded = True

    def _load_from_file(self):
        config_path = Path("config.yaml")
        if not config_path.exists():
            raise FileNotFoundError("config.yaml not found")
        with open(config_path) as f:
            data = yaml.safe_load(f)
        self.data = data

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    @classmethod
    def reset_for_test(cls):
        cls._instance = None
        cls._loaded = False
