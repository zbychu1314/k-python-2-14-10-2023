from django.db import models
from dataclasses import dataclass
from enum import Enum, auto


class MessageType(Enum):
    """
    Class represents messages types
    """

    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()


class Message(models.Model):
    """
    Class represents Message Model
    """

    device_id = models.CharField(max_length=30)
    msg_type = MessageType
    data = models.CharField(max_length=30)

    def __repr__(self):
        return f"{self.device_id},{self.msg_type}, {self.data}"


class Devices(models.Model):
    """
    Class represents messages Devices model
    """

    name = models.CharField(max_length=30)
    device_id = models.CharField(max_length=30)
    type = models.CharField(max_length=8)
    status = models.CharField(max_length=20)

    def __repr__(self):
        return f"{self.name}, {self.device_id}, {self.type}, {self.status}"


class Device(models.Model):
    """
    Class represents messages Device model
    """

    class Meta:
        abstract = True

    def __init__(self) -> None:
        pass

    def connect(self) -> str:
        """
        Abstract function for conneting to device returns result:str

        :returns: result:str
        """
        pass

    def disconnect(self) -> str:
        """
        Abstract function for disconneting to device returns result:str

        :returns: result:str
        """
        pass

    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Abstract function for sending messages

        :input: message_type:MessageType, data:str
        :returns: result:str
        """
        pass

    def status_update(self) -> str:
        """
        Abstract function for showing status of device

        :returns: result:str
        """
        pass


class Hue_Light(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> str:
        """
        Function for conneting to Hue_Light returns result:str

        :returns: result:str
        """
        return "Connecting to Hue Light"

    def disconnect(self) -> str:
        """
        Function for disconneting to Hue_Light returns result:str

        :returns: result:str
        """
        return "Disconnecting to Hue Light"

    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Function for sending messages for Hue_Light

        :input: message_type:MessageType, data:str
        :returns: result:str
        """
        return (
            f"Hue light handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self) -> str:
        """
        Function for showing status of Hue_Light

        :returns: result:str
        """
        napis = "hue_light_status_ok"
        return napis


class SmartSpeaker(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> str:
        """
        Function for conneting to SmartSpeaker returns result:str

        :returns: result:str
        """
        return "Connecting to SmartSpeaker"

    def disconnect(self) -> str:
        """
        Function for disconneting to SmartSpeaker returns result:str

        :returns: result:str
        """
        return "Disconnecting to SmartSpeaker"

    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Function for sending messages for SmartSpeaker

        :input: message_type:MessageType, data:str
        :returns: result:str
        """

        return f"SmartSpeaker handling message of type {message_type.name} with data [{data}]"

    def status_update(self) -> str:
        """
        Function for showing status of SmartSpeaker

        :returns: result:str
        """
        napis = "smart_speaker_status_ok"
        return napis


class Curtains(Device):
    def __init__(self) -> None:
        pass

    def connect(self) -> None:
        """
        Function for conneting to Curtains returns result:str

        :returns: result:str
        """
        return "Connecting to Curtains"

    def disconnect(self) -> None:
        """
        Function for disconneting to Curtains returns result:str

        :returns: result:str
        """
        return "Disconnecting to Curtains"

    def send_message(self, message_type: MessageType, data: str) -> None:
        """
        Function for sending messages for Curtains

        :input: message_type:MessageType, data:str
        :returns: result:str
        """
        return (
            f"Curtains handling message of type {message_type.name} with data [{data}]"
        )

    def status_update(self) -> str:
        """
        Function for showing status of Curtains

        :returns: result:str
        """
        napis = "curtains_status_ok"
        return napis
