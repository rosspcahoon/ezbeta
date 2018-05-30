from django.contrib import admin

# Register your models here.

from .models import Location, Area, Route, Beta

admin.site.register(Location)
admin.site.register(Area)
admin.site.register(Route)
admin.site.register(Beta)

