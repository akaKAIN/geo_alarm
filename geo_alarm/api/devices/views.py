from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from api.devices.serializers import DeviceSerializer
from devices.models import Device


class DeviceCreate(generics.CreateAPIView):
    """Класс создания нового сигнализационного устройства"""
    permission_classes = [permissions.AllowAny]
    queryset = Device.objects.filter(is_active=True)
    serializer_class = DeviceSerializer


class DeviceList(generics.ListAPIView):
    """Класс просмотра списка устройств"""
    permission_classes = [permissions.AllowAny]

    queryset = Device.objects.filter(is_active=True)
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveAPIView):
    """Класс просмотра данных устройства"""
    queryset = Device.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'device': self.object}, template_name='device_detail.html')


