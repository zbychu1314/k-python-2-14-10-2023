from iot.service import IOTService
from iot.devices import *
from iot.message import *


def create_program_wake_up() -> list[Message]:
    t1 = MessageType.SWITCH_ON
    t2 = MessageType.PLAY_SONG
    t3 = MessageType.OPEN
    m1 = Message(device_id=device_ids[0], msg_type=t1, data="Włącz światla")
    m2 = Message(device_id=device_ids[1], msg_type=t1, data="Włącza głośniki")
    m3 = Message(device_id=device_ids[1], msg_type=t2, data="Odgrywa piosenke")
    m4 = Message(device_id=device_ids[2], msg_type=t3, data="Otwiera zasłony")
    list_messages = [m1, m2, m3, m4]
    return list_messages


def create_program_sleep() -> list[Message]:
    t4 = MessageType.SWITCH_OFF
    t5 = MessageType.CLOSE
    m5 = Message(device_id=device_ids[0], msg_type=t4, data="Wyłącz światla")
    m6 = Message(device_id=device_ids[1], msg_type=t4, data="Wyłącza głośniki")
    m7 = Message(device_id=device_ids[2], msg_type=t5, data="Zasłania zasłony")
    list_messages = [m5, m6, m7]
    return list_messages


if __name__ == "__main__":
    iotservice = IOTService()

    #### creation of instances ###

    hue_light = Hue_Light()
    smartspeaker = SmartSpeaker()
    curtains = Curtains()

    #### register devices #######

    iotservice.register_device(hue_light)
    iotservice.register_device(smartspeaker)
    iotservice.register_device(curtains)

    print(iotservice.devices)

    ###### tests devices #########

    iotservice.test_devices()

    ##### TEST unregister device ######

    device_id_input = input("Disconnecting Device_id: ")
    iotservice.unregister_device(device_id=device_id_input)

    print(iotservice.devices)

    # print(iotservice.devices)

    device_ids = []

    for i in range(0, len(iotservice.devices)):
        device_ids.append(list(iotservice.devices[i].keys()))

    ### program wake up ####

    iotservice.run_program(list_messages=create_program_wake_up())

    ### program sleep ####

    iotservice.run_program(list_messages=create_program_sleep())

    ##### TEST get_device #############

    device_id_input = input("Unregister Device_id: ")
    iotservice.get_device(device_id=device_id_input)
    print(iotservice.devices)
