import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Location, Area, Route, Beta

def create_area(area_name):
    location_test = Location.objects.create(location_name='Test location')
    return Area.objects.create(location=location_test, area_name=area_name)
    
def create_route(route_name, days, **kwargs):
    if 'area' in kwargs:
        area_test=kwargs.get('area')
    else:
        area_test = create_area('Test area')
    time = timezone.now() + datetime.timedelta(days=days)
    return Route.objects.create(area=area_test, route_name=route_name, set_date=time)

def create_beta(beta_name, days):
    route_test=create_route('Test route', days)
    time = timezone.now() + datetime.timedelta(days=days)
    return Beta.objects.create(route=route_test,beta_name=beta_name, set_date=time)

class AreaDetailViewTest(TestCase):
    def test_no_routes_area(self):
        area_no_routes = create_area(area_name='No routes area')
        url = reverse('beta:area', args=(area_no_routes.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No routes are available.')

    def test_future_route_area(self):
        area_future_route = create_area(area_name='Future routes area')
        future_route = create_route(route_name='Future route', days=5, area=area_future_route)
        url = reverse('beta:area', args=(area_future_route.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'No routes are available.')


class RouteDetailViewTests(TestCase):
    def test_future_route(self):
        future_route = create_route(route_name='Future route', days=5)
        url = reverse('beta:route', args=(future_route.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'This route is not set yet.')

    def test_past_route(self):
        past_route = create_route(route_name='Past route', days=-5)
        url = reverse('beta:route', args=(past_route.id,))
        response = self.client.get(url)
        self.assertEqual(response.context['route'].route_name, 'Past route')

class BetaDetailViewTests(TestCase):
    def test_future_beta(self):
        future_beta = create_beta(beta_name='Future beta', days=5)
        url = reverse('beta:beta_detail', args=(future_beta.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_beta(self):
        past_beta = create_beta(beta_name='Past beta', days=-5)
        url = reverse('beta:beta_detail', args=(past_beta.id,))
        response = self.client.get(url)
        self.assertEqual(response.context['beta'].beta_name, 'Past beta')
