from rest_framework.pagination import PageNumberPagination


class DeviceListPagination(PageNumberPagination):
    template = 'devices_list.html'

