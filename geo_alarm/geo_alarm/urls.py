from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('', RedirectView.as_view(url='api/v1/device/list/')),

]
