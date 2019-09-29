from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Модель пользователя"""
    class Meta:
        verbose_name = _('Пользователя')
        verbose_name_plural = _('Пользователи')

    address = models.CharField(verbose_name=_('Адресс проживания'), max_length=300, blank=True)
    phone = models.CharField(verbose_name=_('Контактный телефон'), max_length=300, blank=True)

