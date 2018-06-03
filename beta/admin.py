from django.contrib import admin

# Register your models here.

from .models import Location, Area, Route, Beta

class AreaInline(admin.TabularInline):
    model = Area
    extra = 3

class RouteInline(admin.TabularInline):
    model = Route
    extra = 7

class BetaInline(admin.TabularInline):
    model = Beta
    extra = 7

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'longitude', 'latitude')
    fieldsets = [
        (None,                       {'fields': ['location_name', 'location_desc']}),
        ('Geographical Information', {'fields': ['longitude', 'latitude']}),
    ]
    inlines = [AreaInline]

class AreaAdmin(admin.ModelAdmin):
    list_display = ('area_name', 'location', 'area_desc', 'longitude', 'latitude')
    list_filter = ['location']
    fieldsets = [
        (None,                       {'fields': ['location', 'area_name', 'area_desc']}),
        ('Geographical Information', {'fields': ['longitude', 'latitude']}),
    ]
    inlines = [RouteInline]

class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'setter_name', 'grade', 'rating', 'set_date')
    list_filter = ['area']
    fieldsets = [
        (None,                       {'fields': ['area', 'route_name', 'setter_name', 'set_date']}),
        ('Characteristics',          {'fields': ['grade', 'rating']}),
    ]
    inlines = [BetaInline]

admin.site.register(Location, LocationAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Beta)

