from django.urls import path, include

from . import views

urlpatterns = [
	path('', views.index),
    path('assistants', views.assistants),
    path('devices', views.devices),
    path('schedule', views.schedule),
    path('notifications', views.notifications),
    path('hotspot', views.hotspot),
    path('system', views.system),
    path('about', views.about),
]