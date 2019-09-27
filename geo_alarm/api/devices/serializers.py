from rest_framework import serializers

from devices.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    """Модель сигнализационного устройства"""
    class Meta:
        model = Device
        fields = [
            'label',
            'alarm_type',
            'address',
            'latitude',
            'longitude',
            'alarm_range',
        ]

