# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location, Notification
from django.utils import timezone

# Create your tests here.

#To get the info
import json, urllib.request


def loc_detail(id):

    link = urllib.request.urlopen('http://morning-tundra-30769.herokuapp.com/reads/location/'+str(id)+"/")
    data = json.load(link)

    lat = data['Latitude']
    lon = data['Longitude']
    name = data['Name']

    return data


def note_detail(id):

    link = urllib.request.urlopen('http://morning-tundra-30769.herokuapp.com/reads/notification/'+str(id)+"/")
    data = json.load(link)

    l_id = data['LocationID']
    desc= data['Description']
    risk = data['Risk']
    source = data['Source']
    pub_date = data['Date']

    return data


def update_rsu(lat,lon):

    link = urllib.request.urlopen('http://morning-tundra-30769.herokuapp.com/reads/updatersu/'+str(lat)+'/'+str(lon)+'/')

    data = json.load(link)
    notes = []

    for i in range(len(data)):
        notes.append(note_detail(i+1))

    return notes


class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(lat=38.7, lon=-9.23, name="Lisboa")

    def test_location_create(self):
        lisbon = Location.objects.get(name="Lisboa")
        self.assertEqual(lisbon.lat, 38.7)
        self.assertEqual(lisbon.lon, -9.23)
        self.assertEqual(lisbon.name, "Lisboa")


class NotificationTestCase(TestCase):
    def setUp(self):
        lisbon = Location.objects.create(lat=38.7, lon=-9.23, name="Lisboa")
        Notification.objects.create(description="Accident between two bikes", risk=5, source="Waze",
                                    pub_date=timezone.now(), location_id=lisbon.id)

    def test_notification_create(self):
        notif = Notification.objects.get(id=1)
        self.assertEqual(notif.description, "Accident between two bikes")
        self.assertEqual(notif.risk, 5)
        self.assertEqual(notif.source, "Waze")
        self.assertEqual(notif.location.name, "Lisboa")
        self.assertEqual(notif.location.lat, 38.7)
        self.assertEqual(notif.location.lon, -9.23)


# Test remote deploy on heroku
class RemoteDeploy(TestCase):
    def test_loc_detail(self):
        data = loc_detail(1)

        self.assertEqual(data['Name'], "Taguspark")
        self.assertEqual(data['Latitude'], 38.73)
        self.assertEqual(data['Longitude'], -9.29)

    def test_note_detail(self):
        data = note_detail(1)

        l_id = data['LocationID']
        desc = data['Description']
        risk = data['Risk']
        source = data['Source']

        self.assertEqual(l_id, 1)
        self.assertEqual(desc, "Car Accident")
        self.assertEqual(risk, 7)
        self.assertEqual(source, "Waze")

    def test_update_rsu(self):
        data = update_rsu(38.7, -9.23)

        self.assertEqual(len(data), 1)
