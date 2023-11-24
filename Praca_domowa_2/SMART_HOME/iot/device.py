from abc import abstractmethod, abstractclassmethod, ABC
from iot.message import MessageType


class Device(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def connect() -> None:
        pass

    @abstractmethod
    def disconnect() -> None:
        pass

    @abstractmethod
    def send_message(message_type: MessageType, data: str) -> None:
        pass

    @abstractclassmethod
    def status_update(self) -> str:
        pass
