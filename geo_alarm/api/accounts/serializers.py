from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """Модель сигнализационного устройства"""
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'address',
            'password',
        ]
