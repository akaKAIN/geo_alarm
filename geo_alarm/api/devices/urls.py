from django.urls import path
from api.devices.views import DeviceCreate, DeviceList, DeviceDetail, DeviceUpdate, DeviceUpdateAll

urlpatterns = [
    path('create/', DeviceCreate.as_view(), name='device-create'),
    path('list/', DeviceList.as_view(), name='devices-list'),
    path('<int:pk>/', DeviceDetail.as_view(), name='device-detail'),
    path('switch/<int:pk>/', DeviceUpdate.as_view(), name='device-update'),
    path('switch/all/', DeviceUpdateAll.as_view(), name='device-update-all'),

]
