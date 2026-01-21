# serializer.py
class MessageSerializer(ABC):
    @abstractmethod
    def serialize(self, appeal_id: str, status: str, student_name: str) -> str:
        pass
