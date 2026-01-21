# provider_a/client.py
from ..abstract.client import MessengerClient

class ProviderAClient(MessengerClient):
    def send(self, message: str) -> bool:
        # В реальности — API call, но здесь только лог
        print(f"[ProviderA] Отправка: {message}")
        return True
