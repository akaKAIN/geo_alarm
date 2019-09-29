from rest_framework import generics, permissions
from api.accounts.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """Класс создания пользователя"""
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
