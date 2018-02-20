# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from models import Appointment

def index(request):
    return render(request, 'appointments/index.html')

def allAppointments(request):
    json_response =  Appointment.objects.getAppointments()
    return JsonResponse(json_response, safe=False)

def searchAppointments(request):
    json_response =  Appointment.objects.getAppointments(request.GET['search'])
    return JsonResponse(json_response, safe=False)

def submitAppointment(request):
    if request.method == 'GET':
        return redirect('/')
    Appointment.objects.createAppointment(request)
    return redirect('/')

# for dev + test
def cleardb(request):
    Appointment.objects.cleardb()
    return redirect('/')

