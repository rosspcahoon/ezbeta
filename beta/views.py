from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Location, Area, Route, Beta
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'beta/index.html'
    context_object_name = 'location_list'

    # I want to eventually get the nearest locations based on long/lat to the current position
    # and list the top 5
    def get_queryset(self):
        return Location.objects.all()

#class LocationView(generic.ListView):
#    model = Area
#    template_name = 'beta/area.html'
#    context_object_name = 'area_list'

#    def get_queryset(self):
#        return Area.objects.filter()

#class AreaView(generic.ListView):
#    model = Route
#    template_name = 'beta/route.html'
#    context_object_name = 'route_list'

#    def get_queryset(self):
#        return Route.objects.filter()

#class RouteView(generic.ListView):
#    model = Beta
#    template_name = 'beta/beta.html'
#    context_object_name = 'beta_list'

#    def get_queryset(self):
#        return Beta.objects.filter()

def location_detail(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    return render(request, 'beta/area.html', {'location': location})

def area_detail(request, area_id):
    area = get_object_or_404(Area, pk=area_id)
    return render(request, 'beta/route.html', {'area': area})

def route_detail(request, route_id):
    route = get_object_or_404(Route, pk=route_id)
    return render(request, 'beta/beta.html', {'route': route})

def beta_detail(request, beta_id):
    beta = get_object_or_404(Beta, pk=beta_id)
    return render(request, 'beta/beta_detail.html', {'beta': beta})
    
