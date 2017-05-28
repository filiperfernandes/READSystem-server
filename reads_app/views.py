# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.


from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from .models import Location, Notification


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def location_info(request, location_id):
    l = Location.objects.get(id=location_id)

    return JsonResponse({"Latitude": l.lat, "Longitude": l.lon, "Name": l.name})


def list_locations(request):
    list_loc = Location.objects.all()

    response_data = []

    for i in range(len(list_loc)):
        response_data.append({'Latitude': list_loc[i].lat, 'Longitude': list_loc[i].lon, 'Name': list_loc[i].name})

    return JsonResponse(response_data, safe=False)


def notification_info(request, notification_id):
    n = Notification.objects.get(id=notification_id)

    return JsonResponse({"LocationID": n.location.id, "Description": n.description, "Risk": n.risk, "Source": n.source,
                         "Date": n.pub_date})


def list_notifications(request):
    list_n = Notification.objects.all()

    response_data = []

    for i in range(len(list_n)):
        response_data.append({"LocationID": list_n[i].location.id, "Description": list_n[i].description,
                              "Risk": list_n[i].risk, "Source": list_n[i].source, "Date": list_n[i].pub_date})

    return JsonResponse(response_data, safe=False)

# To get the info
# import json, urllib.request
# j = urllib.request.urlopen('http://localhost:8000/reads/location/1/')
# a = json.load(j)
# print (a['Latitude'])
