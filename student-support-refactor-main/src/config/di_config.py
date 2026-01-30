import yaml
from pathlib import Path
from typing import Any

class AppConfig:
    def __init__(self, config_path: str = "config.yaml"):
        self.config_path = config_path
        self.data = self._load()

    def _load(self) -> dict:
        with open(self.config_path) as f:
            return yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)
