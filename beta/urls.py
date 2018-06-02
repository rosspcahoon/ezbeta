from django.urls import path

from . import views

app_name = 'beta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('location/<int:location_id>/', views.LocationAreaList.as_view(), name='location'),
    path('area/<int:area_id>/', views.AreaRouteList.as_view(), name='area'),
    path('route/<int:route_id>/', views.RouteDetailList.as_view(), name='route'),
    path('beta_detail/<int:beta_id>/', views.beta_detail, name='beta_detail'),
]
