from django.contrib import admin
from models import Day, DayLocation
from cities.models import City

class LocationInline(admin.TabularInline):
    model = DayLocation
    raw_id_fields = ['location',]


class DayAdmin(admin.ModelAdmin):
    inlines = [LocationInline,]


admin.site.register(Day, DayAdmin)
