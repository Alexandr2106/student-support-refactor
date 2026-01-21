import yaml
from .request_source import (
    DatabaseRequestSource,
    FileRequestSource,
    WebServiceRequestSource,
    IRequestSource
)

def create_request_source(config_path: str = "config.yaml") -> IRequestSource:
    """
    Фабричный метод: создаёт источник данных на основе конфигурации.
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    source_type = config.get("dataSourceType", "db").lower()

    if source_type == "db":
        return DatabaseRequestSource()
    elif source_type == "file":
        return FileRequestSource()
    elif source_type == "web":
        return WebServiceRequestSource()
    else:
        raise ValueError(f"Неизвестный тип источника: {source_type}")
