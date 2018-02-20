# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime #datetime
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

class AppointmentManager(models.Manager):
  
# getAppointments() function (fetch all + search)

    def getAppointments(self, *args):
        if args:
            search = args[0]
            query = Appointment.objects.filter(Q(description__icontains=search) | Q(date__icontains=search) | Q(formDate__icontains=search) | Q(time__icontains=search) | Q(formTime__icontains=search)).order_by("date", "time") # fetch all appointments ordered by date
        else:
            query = Appointment.objects.order_by("date", "time") # fetch all appointments ordered by date
        temp = serializers.serialize('python', query) # serialize for python
        temp_ref =  [d['fields'] for d in temp] # removing fields
        temp_ref_string =  json.dumps(temp_ref, cls=DjangoJSONEncoder) # set as string
        json_response =  json.loads(temp_ref_string) # set as json
        return json_response

# Create New Appointment + Minimal Validation (prevent blank entries to db)

    def createAppointment(self, request):
        post_data = request.POST
        date = post_data['date']
        time = post_data['time']
        desc = post_data['desc']
        if (len(date)==0) or (len(time)==0) or (len(desc)==0):
            return self
        else:
            date = datetime.strptime(post_data['date'], '%Y-%m-%d')
            time = datetime.strptime(post_data['time'], '%H:%M')
            Appointment.objects.create(
                date = date,
                time = time,
                formDate = date.strftime('%B %-d, %Y'),
                formTime = time.strftime('%-I:%M%p').lower(),
                description = desc
            ) 
        return self

# Edit Appointment (not in reqs)

    def editAppointment(self):
        return self

# Delete Appointment (not in reqs)

    def deleteAppointment(self):
        return (self)

# Development (clear database)

    def cleardb(self):
        Appointment.objects.all().delete()
        return self

# should use single datetime field and combine method (more concise db), but not necessary for scope of assignment
# created_at and updated_at not necessary, unless edit or other functionality included/added
# more efficient ways to handle formatted dates, but for ease of search/query/filter code, doing this
class Appointment(models.Model):
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    formTime = models.CharField(max_length=500, default=' ')
    formDate = models.CharField(max_length=500, default=' ')
    description = models.CharField(max_length=500, default=' ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AppointmentManager()
