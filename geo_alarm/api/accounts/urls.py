from django.urls import path

from api.accounts.views import UserCreate

urlpatterns = [
    path('create/', UserCreate.as_view()),

]
