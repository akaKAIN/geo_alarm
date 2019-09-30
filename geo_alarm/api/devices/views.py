from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponseNotFound
from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from api.devices.paginations import DeviceListPagination
from api.devices.serializers import DeviceSerializer
from devices.models import Device


class AbstractDevice:
    """Абстрактный класс для наследования атрибутов"""
    permission_classes = [permissions.AllowAny]
    queryset = Device.objects.filter(is_active=True).order_by('address')
    serializer_class = DeviceSerializer
    renderer_classes = [TemplateHTMLRenderer]


class DeviceCreate(AbstractDevice, generics.CreateAPIView):
    """Класс создания нового сигнализационного устройства"""

    def post(self, request, *args, **kwargs):
        device = DeviceSerializer(data=request.data)

        if device.is_valid():
            device.save()
        return Response(data={'device': device}, status=201, template_name='device_form.html')


class DeviceList(AbstractDevice, generics.ListAPIView):
    """Класс просмотра списка устройств"""

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Q(label__icontains=search) | Q(address__icontains=search))

        paginator = Paginator(queryset, 7)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

    def get(self, request, *args, **kwargs):
        return Response({'devices': self.get_queryset()}, template_name='devices_list.html')


class DeviceDetail(AbstractDevice, generics.RetrieveAPIView):
    """Класс просмотра данных устройства"""

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'device': self.object}, template_name='device_detail.html')


class DeviceUpdate(generics.UpdateAPIView):
    """Класс для включения или выключения устройства"""
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            try:
                obj = Device.objects.get(pk=self.request.data['pk'])
            except Device.DoesNotExist:
                return Http404

            obj.turn_on = False if obj.turn_on else True
            obj.save()
            return Response(data={'pk': obj.pk}, status=201)
        return Http404

    def get(self, *args, **kwargs):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class DeviceUpdateAll(generics.UpdateAPIView):
    """Класс включения и выключения всех устройств разом"""
    permission_classes = [permissions.AllowAny]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    def post(self, *args, **kwargs):
        switch = self.request.data['switch']
        if switch == 'switch_on':
            Device.objects.update(turn_on=True)
        elif switch == 'switch_off':
            Device.objects.update(turn_on=False)
        return Response(data={}, status=201)




