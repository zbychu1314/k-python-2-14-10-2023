from django.shortcuts import render
from iot_control.models import Devices
from .services import IOTService as service
from django.http import Http404
from .models import Hue_Light, Curtains, SmartSpeaker

# Create your views here.
# Create your views here.


def show_list(request):
    """
    Function returns Return a HttpResponse - list of IOT Devices

    :returns: HttpResponse
    """

    if request.method == "GET":
        p = service.show_list()

        return render(request, "iot_control/list.html", {"iot_control": p})

    if request.method == "POST":
        if "_register" in request.POST:
            m, command_output = service.register_device(
                name=request.POST.get("pos_name"), type=request.POST.get("pos_type")
            )

            p = service.show_list()

        elif "_unregister" in request.POST:
            m, command_output = service.unregister_device(
                device_id=request.POST.get("pos_device_id")
            )

        elif "_run_program" in request.POST:
            command_output_list = service.run_program(
                program_name=request.POST.get("pos_program_name")
            )
            p = service.show_list()
            return render(
                request,
                "iot_control/list.html",
                {"iot_control": p, "command_output": command_output_list},
            )

        p = service.show_list()

    return render(
        request,
        "iot_control/list.html",
        {"iot_control": p, "command_output": command_output},
    )


def details(request, id):
    """
    Function returns Return a HttpResponse - details of IOT Device

    :returns: HttpResponse
    """

    try:
        p = service.get(id)

    except:
        raise Http404

    return render(request, "iot_control/iot_control_details.html", {"iot_control": p})


def connect(request, id):
    """
    Function returns Return a HttpResponse - function for connecting to IOT Devices

    :returns: HttpResponse
    """
    device = None
    try:
        p = service.get(id)
        if p.type == "hue_light":
            device = Hue_Light()
        elif p.type == "smartspeaker":
            device = SmartSpeaker()
        elif p.type == "curtains":
            device = Curtains()
    except:
        raise Http404

    return render(
        request,
        "iot_control/iot_control_status.html",
        {"iot_control": p, "Status": device.connect(), "Action": "Connect"},
    )


def disconnect(request, id):
    """
    Function returns Return a HttpResponse - function for disconnecting IOT Devices

    :returns: HttpResponse
    """

    device = None
    try:
        p = service.get(id)
        if p.type == "hue_light":
            device = Hue_Light()
        elif p.type == "smartspeaker":
            device = SmartSpeaker()
        elif p.type == "curtains":
            device = Curtains()
    except:
        raise Http404

    return render(
        request,
        "iot_control/iot_control_status.html",
        {"iot_control": p, "Status": device.disconnect(), "Action": "Disconnect"},
    )


def status_update(request, id):
    """
    Function returns Return a HttpResponse - function for showing status of IOT Devices

    :returns: HttpResponse
    """

    device = None
    try:
        p = service.get(id)
        if p.type == "hue_light":
            device = Hue_Light()
        elif p.type == "smartspeaker":
            device = SmartSpeaker()
        elif p.type == "curtains":
            device = Curtains()
    except:
        raise Http404

    return render(
        request,
        "iot_control/iot_control_status.html",
        {"iot_control": p, "Status": device.status_update(), "Action": "Status_Update"},
    )


def execute_test_diagnostics(request):
    """
    Function returns Return a HttpResponse - function for executing diagnostincs of IOT Devices

    :returns: HttpResponse
    """

    if request.method == "GET":
        p = service.show_list()
        data = service.test_devices()

    return render(
        request,
        "iot_control/iot_control_diagnostics.html",
        {"iot_control": p, "Status": data},
    )


def unregister(request, device_id):
    """
    Function returns Return a HttpResponse - function for unregistering IOT Devices

    :returns: HttpResponse
    """
    if request.method == "POST":
        service.unregister_device(device_id=request.POST.get("pos_device_id"))
        p = service.show_list()

    return render(request, "iot_control/list.html", {"iot_control": p})
