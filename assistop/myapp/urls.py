from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index),
    path('assistants', views.assistants),
    path('assistants/toggle/<str:ipv4>', views.toggle),
    path('assistants/name/<str:ipv4>', views.nameAssistant),
    path('assistants/remove/<str:ipv4>', views.removeAssistant),
    path('devices', views.devices),
    path('devices/name/<str:ipv4>', views.nameDevice),
    path('devices/remove/<str:ipv4>', views.removeDevice),
    path('schedule', views.schedule),
    path('notifications', views.notifications),
    path('hotspot', views.hotspot),
    path('system', views.system),
    path('about', views.about),
]