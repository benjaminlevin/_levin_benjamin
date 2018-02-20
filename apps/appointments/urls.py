from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^all_appointments$', views.allAppointments),
    url(r'^search$', views.searchAppointments),
    url(r'^submit_appointment$', views.submitAppointment),
    url(r'^cleardb$', views.cleardb), # for development only
]