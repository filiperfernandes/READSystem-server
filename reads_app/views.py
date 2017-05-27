# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import urllib

from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from .models import Location, Notification


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def location_info(request, location_id):
    l = Location.objects.get(id=location_id)

    return JsonResponse({"Latitude": l.lat, "Longitude":l.lon, "Name": l.name})


def list_locations(request):

    list = Location.objects.all()

    response_data = []
    temp_dict = {'Latitude': 0.0, 'Longitude': 0.0, 'Name': "default"}

    for i in range(len(list)):
        temp_dict['Latitude'] = list[i].lat
        temp_dict['Longitude'] = list[i].lon
        temp_dict['Name'] = list[i].name
        response_data.append(temp_dict)

    return JsonResponse(response_data, safe=False)


def notification_info(request, notification_id):
    n = Notification.objects.get(id=notification_id)

    return JsonResponse({"LocationID": n.location.id, "Description": n.description, "Risk": n.risk, "Source": n.source, "Date": n.pub_date})


def list_notifications(request):
    list = Notification.objects.all()

    response_data = []
    temp_dict = {"LocationID": 0, "Description": "empty", "Risk": 0, "Source": "john doe", "Date": timezone.now()}

    for i in range(len(list)):
        temp_dict['LocationID'] = list[i].location.id
        temp_dict['Description'] = list[i].description
        temp_dict['Risk'] = list[i].risk
        temp_dict['Source'] = list[i].source
        temp_dict['Date'] = list[i].pub_date
        response_data.append(temp_dict)

    return JsonResponse(response_data, safe=False)



# To get the info
# import json, urllib.request
# j = urllib.request.urlopen('http://localhost:8000/reads/1/location/')
# a = json.load(j)
# print (a['Latitude'])
