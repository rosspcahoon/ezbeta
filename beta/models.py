import datetime

from django.db import models
from django.utils import timezone
from collections import namedtuple

# Create your models here.

class Location(models.Model):
    ''' Describes the location where the climbing routes are located.
    This will include long/lat coordinates, and will be able to be searched
    by proximity '''
    location_name = models.CharField(max_length=50, default='Missing location name')
    location_desc = models.CharField(max_length=500, default='')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    def __str__(self):
        return self.location_name

class Area(models.Model):
    ''' Describes the sublocations within a Location. For example,
    in a boulder field, this might refer to individual boulders. '''
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=50, default='')
    area_desc = models.CharField(max_length=500, default='')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    def __str__(self):
        return self.area_name

class Route(models.Model):
    ''' Describes physical routes on the area '''
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=50, default='')
    setter_name = models.CharField(max_length=100, default='')
    grade = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    set_date = models.DateTimeField('date set', default = timezone.now)
    def __str__(self):
        return self.route_name

class Beta(models.Model):
    ''' Describes one way to do the beta for a specific route '''
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    beta_name = models.CharField(max_length=50, default='')
    beta_desc = models.CharField(max_length=500, default='')
    quality_rating = models.IntegerField(default=0)
    creator_name = models.CharField(max_length=50, default='')
    set_date = models.DateTimeField('date set', default = timezone.now)
    def __str__(self):
        return self.beta_name
