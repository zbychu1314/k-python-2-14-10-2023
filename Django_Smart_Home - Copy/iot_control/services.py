import random
import string
from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from .models import Devices as ModelDevices
from .models import Message as ModelMessage
from .models import *
from .models import Device


class ModelDevicesNotFound(Exception):
    pass


@dataclass
class DevicesDTO:  # DTO - data transfer object
    '''
    DTO class for Model Devices
    '''
    id: int
    name: str
    device_id: str
    type: str
    status: str

    @classmethod
    def from_django_model(cls, m: ModelDevices) -> "DevicesDTO":
        '''
        Function converts Devices Model into Devices DTO

        input: ModelDevices
        return: DevicesDTO
        '''
        return DevicesDTO(
            id=m.id, name=m.name, device_id=m.device_id, type=m.type, status=m.status
        )


@dataclass
class MessageDTO:  # DTO - data transfer object
    '''
    DTO class for Model Messages
    '''
    device_id: str
    msg_type: MessageType
    data: str

    @classmethod
    def from_django_model(cls, m: ModelMessage) -> "MessageDTO":
        '''
        Function converts Messages Model into Messages DTO

        input: MessagesDevices
        return: DevicesDTO
        '''
        return MessageDTO(device_id=m.device_id, msg_type=m.msg_type, data=m.data)


class ISmartService(ABC):
    @abstractclassmethod
    def show_list(cls) -> list[DevicesDTO]:
        """
        Abstract function returns list of DTO Devices

        :returns: list DevicesDTO
        """
        pass

    @abstractclassmethod
    def get(cls, id: int) -> DevicesDTO:
        """
        Abstract function returns list of specific instance of DevicesDTO

        :returns: DevicesDTO
        """
        pass

    @abstractclassmethod
    def register_device(cls, name: str, type: str) -> DevicesDTO:
        """
        Abstract function register new elemnent, returns list of specific instance of DevicesDTO
        
        :input: name:str, type:str
        :returns: DevicesDTO
        """
        pass
    
    @abstractclassmethod
    def unregister_device(cls, device_id: str) -> tuple[list[DevicesDTO], str]:
        """
        Abstract function unregister elemnent of class DevicesDTO, returns list of specific instance of DevicesDTO, 
         and message
        
        :input: name:str, type:str
        :returns: DevicesDTO
        """
        pass

    
    @abstractclassmethod
    def run_program(cls, program_name: str) -> list[Message]:
        """
        Abstract function for executing message program
        
        :input: program_name:str
        :returns: list of Messages: list[Message]
        """
        pass
    
    @abstractclassmethod
    def test_devices(cls) -> str:
        """
        Abstract function for executing diagnoscics
        
        :input: 
        :returns: results:str
        """
        pass

    @abstractclassmethod
    def generate_id(cls, number: int) -> str:
        """
        Abstract function for generating ID
        
        :input: number:int
        :returns: results:str
        """
        pass


class IOTService(ISmartService):
    @classmethod
    def show_list(cls) -> list[DevicesDTO]:
        """
        Function returns list of DTO Devices

        :returns: list DevicesDTO
        """
        devices: list[DevicesDTO] = [
            DevicesDTO.from_django_model(m) for m in ModelDevices.objects.all()
        ]
        return devices

    @classmethod
    def register_device(cls, name: str, type: str) -> DevicesDTO:
        """
        Function register new elemnent, returns list of specific instance of DevicesDTO
        
        :input: name:str, type:str
        :returns: DevicesDTO
        """
        device = None
        type=type.lower()
        if type == "hue_light":
            device = Hue_Light()
        elif type == "smartspeaker":
            device = SmartSpeaker()
        elif type == "curtains":
            device = Curtains()
        else:
            connect_output = "Error: You selected wrong type"
            return ModelDevices.objects.all(), connect_output

        connect_output = device.connect()

        m = ModelDevices.objects.create(
            name=name,
            device_id=cls.generate_id(4),
            type=type,
            status=device.status_update(),
        )

        return DevicesDTO.from_django_model(m), connect_output

    @classmethod
    def get(cls, id: int) -> DevicesDTO:
        """
        Function returns list of specific instance of DevicesDTO

        :returns: DevicesDTO
        """
        try:
            return DevicesDTO.from_django_model(ModelDevices.objects.get(id=id))
        except ModelDevices.DoesNotExist:
            pass

        raise ModelDevicesNotFound

    @classmethod
    def unregister_device(cls, device_id: str) -> tuple[list[DevicesDTO], str]:
        """
        Function unregister elemnent of class DevicesDTO, returns list of specific instance of DevicesDTO, 
        and message
        
        :input: name:str, type:str
        :returns: DevicesDTO
        """
        try:
            devices = cls.show_list()
            type = None
            device = None
            device_id = device_id.upper()
            for entry in devices:
                if device_id == entry.device_id:
                    type = entry.type
                    break
            if type is None:
                m = ModelDevices.objects.all()
                connect_output = 'Error: Device_ID not found'
                return m, connect_output
            if type == "hue_light":
                device = Hue_Light()
            elif type == "smartspeaker":
                device = SmartSpeaker()
            elif type == "curtains":
                device = Curtains()
            connect_output = device.disconnect()
            m = ModelDevices.objects.filter(device_id=device_id).delete()
            return m, connect_output

        except ModelDevices.DoesNotExist:
            pass
        raise ModelDevicesNotFound

    @classmethod
    def run_program(cls, program_name: str) -> list[Message]:

        """
        Function for executing specific message program
        
        :input: program_name:str
        :returns: list of Messages: list[Message]
        """
        devices = cls.show_list()
        list_messages = []
        dev_hue = Hue_Light()
        dev_speaker = SmartSpeaker()
        dev_curtains = Curtains()
        program_name=program_name.lower()
        if program_name =='wake_up':
            t1 = MessageType.SWITCH_ON
            t2 = MessageType.PLAY_SONG
            t3 = MessageType.OPEN
            for device in devices:
                if device.type == "hue_light":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t1, data="Włącz światla"
                    )
                    list_messages.append(dev_hue.send_message(m.msg_type, m.data))
                elif device.type == "smartspeaker":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t1, data="Włącz głośniki"
                    )
                    list_messages.append(dev_speaker.send_message(m.msg_type, m.data))
                    m = MessageDTO(
                        device_id=device.type, msg_type=t2, data="Odgrywa piosenke"
                    )
                    list_messages.append(dev_speaker.send_message(m.msg_type, m.data))
                elif device.type == "curtains":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t3, data="Otwiera zasłony"
                    )
                    list_messages.append(dev_curtains.send_message(m.msg_type, m.data))
            return list_messages
        elif program_name == 'sleep':
            t4 = MessageType.SWITCH_OFF
            t5 = MessageType.CLOSE
            for device in devices:
                if device.type == "hue_light":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t4, data="Wyłącz światla"
                    )
                    list_messages.append(dev_hue.send_message(m.msg_type, m.data))
                elif device.type == "smartspeaker":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t4, data="Wyłącz głośniki"
                    )
                    list_messages.append(dev_speaker.send_message(m.msg_type, m.data))
                elif device.type == "curtains":
                    m = MessageDTO(
                        device_id=device.type, msg_type=t5, data="Zasłania zasłony"
                    )
                    list_messages.append(dev_curtains.send_message(m.msg_type, m.data))
            print(f"LIST MESSAGES: {list_messages}")
            return list_messages
        else:
            list_messages = 'Error: Selected program is not supported yet ;) Chose wake_up or sleep'
            return list_messages
    @classmethod
    def test_devices(cls) -> str:
        """
        Function for executing diagnoscics
        
        :input: 
        :returns: results:str
        """

        raw_data = []
        print("Start test devices")
        raw_data.append("Start test devices")
        print("Connecting to diagnostics server")
        raw_data.append("Connecting to diagnostics server")
        devices = cls.show_list()
        for device in devices:
            napis = device.status
            name = device.name
            raw_data.append(
                f"Device Name: {name}, Sending status update {napis} to server"
            )
        return raw_data

    @classmethod
    def generate_id(cls, number: int) -> str:
        """
        Function for generating ID
        
        :input: number:int
        :returns: results:str
        """
        course_letters = ""
        for _ in range(number):
            course_letters += random.choice(string.ascii_uppercase)
        return course_letters
