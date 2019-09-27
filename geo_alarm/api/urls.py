
from django.urls import path, include


urlpatterns = [
    path('device/', include('api.devices.urls')),

]
