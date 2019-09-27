from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'alarm_type',
        'alarm_range',
        'latitude',
        'longitude',
    ]


admin.site.register(Device, DeviceAdmin)