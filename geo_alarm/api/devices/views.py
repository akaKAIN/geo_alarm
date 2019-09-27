from rest_framework import generics, permissions

from api.devices.serializers import DeviceSerializer
from devices.models import Device


class DeviceCreate(generics.CreateAPIView):
    """Класс создания нового сигнализационного устройства"""
    permission_classes = [permissions.AllowAny]
    queryset = Device.objects.filter(is_active=True)
    serializer_class = DeviceSerializer


class DeviceList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Device.objects.filter(is_active=True)
    serializer_class = DeviceSerializer



