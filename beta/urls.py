from django.urls import path

from . import views

app_name = 'beta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
#    path('<str:location_name>/', views.location_detail, name='area'),
#    path('<str:location_name>/<str:area_name>/', views.area_detail, name='route'),
#    path('<str:location_name>/<str:area_name>/<str:route_name>/', views.route_detail, name='beta'),
#    path('<str:location_name>/<str:area_name>/<str:route_name>/<str:beta_name>/', views.beta_detail, name='beta_detail'),
    path('location/<int:location_id>/', views.location_detail, name='area'),
    path('area/<int:area_id>/', views.area_detail, name='route'),
    path('route/<int:route_id>/', views.route_detail, name='beta'),
    path('beta_detail/<int:beta_id>/', views.beta_detail, name='beta_detail'),
]
