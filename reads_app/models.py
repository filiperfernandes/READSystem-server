# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Location(models.Model):
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Notification(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    risk = models.IntegerField(default=0)
    source = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "Something happened at: " + self.location.name + self.description
