from django.db import models
from django.utils.translation import gettext_lazy as _


class Device(models.Model):
    """Модель сигнализационного устройства"""
    class Meta:
        verbose_name_plural = _('Устройства')
        verbose_name = _('Устройство')

    TYPE_DEVICE = (
        ('siren', _('сирена')),
        ('speaker', _('громкоговоритель')),
    )
    label = models.CharField(verbose_name=_('Маркировка устройства'), max_length=300, blank=True)
    alarm_type = models.CharField(verbose_name=_('Тип устройства'), max_length=20, choices=TYPE_DEVICE)
    address = models.CharField(verbose_name=_(' Адрес устройства'), max_length=300, blank=True)
    latitude = models.DecimalField(verbose_name=_('Широта'), max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name=_('Долгота'), max_digits=9, decimal_places=6)
    alarm_range = models.PositiveIntegerField(verbose_name=_('Радиус действия (метров)'))
    is_active = models.BooleanField(verbose_name=_('Подключено ли устройство.'), default=True)
    turn_on = models.BooleanField(verbose_name=_('Состояние "Вкл./выкл"'), default=False)

    def __str__(self):
        no_label = f'{self.alarm_type.title()} {_("на")} {self.address[:20]}..'
        return f'{self.label if self.label else no_label}, {_("радиус")}: {self.alarm_range}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    def switch_on(self):
        self.turn_on = True
        self.save()

    def switch_off(self):
        self.turn_on = False
        self.save()

