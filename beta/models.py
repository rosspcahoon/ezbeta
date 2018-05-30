import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    ''' Describes the location where the climbing routes are located.
    This will include long/lat coordinates, and will be able to be searched
    by proximity '''
    location_name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.location_name

class Area(models.Model):
    ''' Describes the sublocations within a Location. For example,
    in a boulder field, this might refer to individual boulders. '''
    
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=200)
    def __str__(self):
        return self.area_name

class Route(models.Model):
    ''' Describes physical routes on the area '''
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=200)
    grade = models.IntegerField(default=0)
    def __str__(self):
        return self.route_name

class Beta(models.Model):
    ''' Describes one way to do the beta for a specific route '''
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    beta_name = models.CharField(max_length=200)
    beta_text = models.CharField(max_length=500)
    def __str__(self):
        return self.beta_name
