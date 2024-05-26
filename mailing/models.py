from datetime import datetime

import pytz
from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {"blank": True, "null": True}
zone = pytz.timezone(settings.TIME_ZONE)


class ClientService(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name="Почта")
    name = models.CharField(max_length=100, verbose_name="ФИО")
    comments = models.TextField(verbose_name="Комментарий", **NULLABLE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользватель", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ("id",)


class MessageMailing(models.Model):
    subject_line = models.CharField(max_length=150, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Текс сообщения", **NULLABLE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользватель", null=True
    )

    def __str__(self):
        return self.subject_line

    class Meta:
        verbose_name = "Сообщение рассылки"
        verbose_name_plural = "Сообщения рассылки"
        ordering = ("id",)


class Mailing(models.Model):

    class PeriodMailing(models.TextChoices):
        ONE_DAY = "Раз в день", "Раз в день"
        ONE_WEEK = "Раз в неделю", "Раз в неделю"
        ONE_MONTH = "Раз в месяц", "Раз в месяц"

    class StatusMailing(models.TextChoices):
        CREATED = "Создана", "Создана"
        STARTED = "Запущена", "Запущена"
        COMPLETED = "Завершена", "Завершена"

    create_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время создания рассылки рассылки"
    )
    quit_at = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время окончания работы рассылки"
    )
    next_send_time = models.DateTimeField(
        default=timezone.now, verbose_name="Дата и время отправки рассылки"
    )
    period_mailing = models.CharField(
        max_length=50,
        default=PeriodMailing.ONE_DAY.value,
        choices=PeriodMailing.choices,
        verbose_name="Периодичность рассылки",
    )
    status_mailing = models.CharField(
        max_length=50,
        default=StatusMailing.CREATED.value,
        choices=StatusMailing.choices,
        verbose_name="Статус рассылки",
    )
    client = models.ManyToManyField(ClientService, verbose_name="Клиенты рассылки")
    message = models.ForeignKey(
        MessageMailing, on_delete=models.CASCADE, verbose_name="Сообщение", **NULLABLE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользватель", null=True
    )

    def __str__(self):
        return str(self.create_at)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ("id",)
        permissions = (
            ("cancel_mailing_status_mailing", "Can cancel mailing status_mailing"),
        )


class MailingAttempt(models.Model):
    date_last_mailing = models.DateTimeField(
        verbose_name="Дата и время последней рассылки", auto_now_add=True
    )
    status_mailing = models.BooleanField(verbose_name="Статус рассылки")
    server_response = models.CharField(verbose_name="Ответ сервера", **NULLABLE)
    mailing = models.ForeignKey(
        Mailing, verbose_name="Рассылки", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.date_last_mailing)

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
        ordering = ("id",)
