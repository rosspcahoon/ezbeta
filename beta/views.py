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

class LocationAreaList(generic.ListView):
    
    template_name = 'beta/area.html'
    context_object_name = 'area_list' 

    def get_queryset(self):
        self.location = get_object_or_404(Location, pk=self.kwargs['location_id'])
        return Area.objects.filter(location=self.location)

class AreaRouteList(generic.ListView):

    template_name = 'beta/route.html'
    context_object_name = 'route_list'

    def get_queryset(self):
        self.area = get_object_or_404(Area, pk=self.kwargs['area_id'])
        return Route.objects.filter(area=self.area, set_date__lte=timezone.now())

#def route_detail(request, route_id):
#    route = get_object_or_404(Route, pk=route_id, set_date__lte=timezone.now())
#    return render(request, 'beta/beta.html', {'route': route})

class RouteDetailList(generic.ListView):

    template_name = 'beta/beta.html'
    context_object_name = 'beta_list'
    
    def get_queryset(self):
        self.route = get_object_or_404(Route, pk=self.kwargs['route_id'])
        return Beta.objects.filter(route=self.route, set_date__lte=timezone.now())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['route'] = self.route
        context['grade'] = self.route.grade
        context['rating'] = self.route.rating
        context['set_date'] = self.route.set_date
        context['now'] = timezone.now()
        return context


def beta_detail(request, beta_id):
    beta = get_object_or_404(Beta, pk=beta_id, set_date__lte=timezone.now())
    return render(request, 'beta/beta_detail.html', {'beta': beta})
    
