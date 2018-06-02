from django.contrib import admin

# Register your models here.

from .models import Location, Area, Route, Beta

class AreaInline(admin.TabularInline):
    model = Area
    extra = 3

class RouteInline(admin.TabularInline):
    model = Route
    extra = 7

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                       {'fields': ['location_name', 'location_desc']}),
        ('Geographical Information', {'fields': ['longitude', 'latitude']}),
    ]
    inlines = [AreaInline]

admin.site.register(Location, LocationAdmin)
admin.site.register(Area)
admin.site.register(Route)
admin.site.register(Beta)

