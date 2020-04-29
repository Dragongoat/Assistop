from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import os
import json
import subprocess
from . import forms

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def index(request):
	context={
		"title": "Assistop: Dashboard",
	}
	return render(request, "index.html", context = context)

def assistants(request):
    with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
        d = json.load(f)
        controlledDic = d['controlledDevices']
        context={
            "title": "Assistop: My Assistants",
            "controlledDevices": controlledDic,
        }
    return render(request, "assistants.html", context=context)

def toggle(request, ipv4):
    with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
        d = json.load(f)
        controlledDic = d['controlledDevices']
        for device in controlledDic:
            if device["IPv4"] == ipv4:
                path = os.getcwd()
                script_path = os.path.join(BASE_DIR, 'myapp/runSSH.sh')
                if device["online"] == 1:
                    subprocess.run([script_path, ipv4, "D"])
                    device["online"] = 0
                else:
                    subprocess.run([script_path, ipv4, "A"])
                    device["online"] = 1
        d['controlledDevices'] = controlledDic

    with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json'), "w") as f:
        json.dump(d, f)
    return redirect("/assistants")

def nameAssistant(request, ipv4):
    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
                d = json.load(f)
                controlledDic = d['controlledDevices']
                for device in controlledDic:
                    if device["IPv4"] == ipv4:
                        device["UserName"] = form.cleaned_data['dev_name']
                d['controlledDevices'] = controlledDic

            with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json'), "w") as f:
                json.dump(d, f)
            return HttpResponseRedirect('/assistants')

def removeAssistant(request, ipv4):
    with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
        d = json.load(f)
        controlledDic = d['controlledDevices']
        for i, device in enumerate(controlledDic):
            if device["IPv4"] == ipv4:
                del controlledDic[i]
        d['controlledDevices'] = controlledDic

        with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json'), "w") as f:
            json.dump(d, f)
        return HttpResponseRedirect('/assistants')

def devices(request):
	with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
		d = json.load(f)
		controllerDic = d['controllerDevices']
		context={
			"title": "Assistop: My Devices",
			"controllerDevices": controllerDic,
		}
		return render(request, "devices.html", context=context)

def nameDevice(request, ipv4):
    if request.method == 'POST':
        form = forms.NameForm(request.POST)
        if form.is_valid():
            with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
                d = json.load(f)
                controllerDic = d['controllerDevices']
                for device in controllerDic:
                    if device["IPv4"] == ipv4:
                        device["UserName"] = form.cleaned_data['dev_name']
                d['controllerDevices'] = controllerDic

            with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json'), "w") as f:
                json.dump(d, f)
            return HttpResponseRedirect('/devices')

def removeDevice(request, ipv4):
    with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json')) as f:
        d = json.load(f)
        controllerDic = d['controllerDevices']
        for i, device in enumerate(controllerDic):
            if device["IPv4"] == ipv4:
                del controllerDic[i]
        d['controllerDevices'] = controllerDic

        with open(os.path.join(BASE_DIR, 'myapp/documentation/JSON/devices.json'), "w") as f:
            json.dump(d, f)
        return HttpResponseRedirect('/devices')

def schedule(request):
    context={
        "title": "Assistop: Schedule",
    }
    return render(request, "schedule.html", context=context)

def notifications(request):
    context={
        "title": "Assistop: Notifications",
    }
    return render(request, "notifications.html", context=context)

def hotspot(request):
    context={
        "title": "Assistop: Hotspot",
    }
    return render(request, "hotspot.html", context=context)

def system(request):
    context={
        "title": "Assistop: System",
    }
    return render(request, "system.html", context=context)

def about(request):
    context={
        "title": "Assistop: About",
    }
    return render(request, "about.html", context=context)
