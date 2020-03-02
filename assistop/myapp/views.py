from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context={
		"title": "Assistop: Dashboard",
	}
	return render(request, "index.html", context = context)

def assistants(request):
    context={
        "title": "Assistop: My Assistants",
    }
    return render(request, "assistants.html", context=context)

def devices(request):
    context={
        "title": "Assistop: My Devices",
    }
    return render(request, "devices.html", context=context)

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