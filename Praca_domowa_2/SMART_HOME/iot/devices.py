from iot.device import Device
from iot.message import MessageType


class Hue_Light(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        print("Connecting to Hue Light")

    def disconnect(self) -> None:
        print("Disconnecting to Hue Light")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Hue light handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self) -> str:
        napis = "hue_light_status_ok"
        return napis


class SmartSpeaker(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        print("Connecting to SmartSpeaker")

    def disconnect(self) -> None:
        print("Disconnecting to SmartSpeaker")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"SmartSpeaker handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self) -> str:
        napis = "smart_speaker_status_ok"
        return napis


class Curtains(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        print("Connecting to Curtains")

    def disconnect(self) -> None:
        print("Disconnecting to Curtains")

    def send_message(self, message_type: MessageType, data: str) -> None:
        print(
            f"Curtains handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self) -> str:
        napis = "curtains_status_ok"
        return napis
