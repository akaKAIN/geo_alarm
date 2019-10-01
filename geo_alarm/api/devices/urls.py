from django.urls import path
from api.devices.views import DeviceCreate, DeviceList, DeviceDetail, DeviceSwitch, DeviceSwitchAll, DeviceUpdate, \
    DeviceDelete

urlpatterns = [
    path('create/', DeviceCreate.as_view(), name='device-create'),
    path('list/', DeviceList.as_view(), name='devices-list'),
    path('<int:pk>/', DeviceDetail.as_view(), name='device-detail'),
    path('switch/<int:pk>/', DeviceSwitch.as_view(), name='device-switch'),
    path('switch/all/', DeviceSwitchAll.as_view(), name='device-switch-all'),
    path('update/<int:pk>/', DeviceUpdate.as_view(), name='device-update'),
    path('delete/<int:pk>/', DeviceDelete.as_view(), name='device-delete')

]
