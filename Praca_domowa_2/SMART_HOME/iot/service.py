import random
import string
from iot.device import Device
from iot.message import Message
from iot.diagnostics import collect_diagnostics


class IOTService:
    def __init__(self) -> None:
        self.devices = []

    def register_device(self, device: Device):
        device.connect()
        device_id = self.generate_id(4)
        self.devices.append({device_id: device})

    def unregister_device(self, device_id: str) -> None:
        for entry in self.devices:
            for key, val in entry.items():
                if key == device_id:
                    val.disconnect()

    def get_device(self, device_id: str) -> None:
        for entry in self.devices:
            for key, val in entry.items():
                if key == device_id:
                    self.devices.remove({key: val})

    def run_program(self, list_messages: list[Message]):
        print("======RUNNING PROGRAM======")
        for mes in list_messages:
            device_id = mes.device_id[0]
            for entry in self.devices:
                for key, val in entry.items():
                    if key == device_id:
                        val.send_message(message_type=mes.msg_type, data=mes.data)
        print("======END OF PROGRAM======")

    def test_devices(self):
        print("Start test devices")
        for entry in self.devices:
            for key, val in entry.items():
                collect_diagnostics(device=val)

    @staticmethod
    def generate_id(number: int) -> str:
        course_letters = ""
        for _ in range(number):
            course_letters += random.choice(string.ascii_uppercase)
        return course_letters
