from django.urls import path
from api.devices.views import DeviceCreate, DeviceList, DeviceDetail

urlpatterns = [
    path('create/', DeviceCreate.as_view()),
    path('list/', DeviceList.as_view()),
    path('<int:pk>/', DeviceDetail.as_view(), name='device-detail'),

]
