import yaml
from pathlib import Path
from infrastructure.notifications.factories import ProviderAFactory, ProviderBFactory
from infrastructure.notifications.factories import AbstractMessengerFactory

def load_config():
    with open(Path(__file__).parent / "../config.yaml") as f:
        return yaml.safe_load(f)

def get_data_source_type() -> str:
    return load_config()["dataSourceType"]

def get_messenger_factory() -> AbstractMessengerFactory:
    provider = load_config().get("messengerProvider", "ProviderA")
    if provider == "ProviderA":
        return ProviderAFactory()
    elif provider == "ProviderB":
        return ProviderBFactory()
    else:
        raise ValueError(f"Неизвестный провайдер: {provider}")
