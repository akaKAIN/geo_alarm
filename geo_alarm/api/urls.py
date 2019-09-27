
from django.urls import path, include


urlpatterns = [
    path('devices/', include('api.devices.urls')),

]
