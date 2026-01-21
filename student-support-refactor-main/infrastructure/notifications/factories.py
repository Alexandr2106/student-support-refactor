from abc import ABC, abstractmethod
from .abstract import MessengerClient, Authentication, MessageSerializer, ErrorHandler

class AbstractMessengerFactory(ABC):
    @abstractmethod
    def create_client(self) -> MessengerClient: ...
    @abstractmethod
    def create_auth(self) -> Authentication: ...
    @abstractmethod
    def create_serializer(self) -> MessageSerializer: ...
    @abstractmethod
    def create_error_handler(self) -> ErrorHandler: ...

# Конкретные фабрики
from .provider_a import ProviderAClient, ProviderAAuth, ProviderASerializer, ProviderAErrorHandler
from .provider_b import ProviderBClient, ProviderBAuth, ProviderBSerializer, ProviderBErrorHandler

class ProviderAFactory(AbstractMessengerFactory):
    def create_client(self): return ProviderAClient()
    def create_auth(self): return ProviderAAuth()
    def create_serializer(self): return ProviderASerializer()
    def create_error_handler(self): return ProviderAErrorHandler()

class ProviderBFactory(AbstractMessengerFactory):
    def create_client(self): return ProviderBClient()
    def create_auth(self): return ProviderBAuth()
    def create_serializer(self): return ProviderBSerializer()
    def create_error_handler(self): return ProviderBErrorHandler()
