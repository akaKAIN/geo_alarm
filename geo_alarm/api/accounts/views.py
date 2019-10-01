from rest_framework import generics, permissions, serializers
from api.accounts.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """Класс создания пользователя"""
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        return super().create(request, *args, **kwargs)