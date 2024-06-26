# Generated by Django 4.2 on 2024-05-17 11:42

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=150, unique=True, verbose_name="Почта"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="ФИО")),
                (
                    "comments",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        default=datetime.datetime.now,
                        verbose_name="Дата и время отправки рассылки",
                    ),
                ),
                (
                    "period_mailing",
                    models.CharField(
                        choices=[
                            ("Раз в день", "Раз в день"),
                            ("Раз в неделю", "Раз в неделю"),
                            ("Раз в месяц", "Раз в месяц"),
                        ],
                        default="Раз в день",
                        max_length=50,
                        verbose_name="Периодичность рассылки",
                    ),
                ),
                (
                    "status_mailing",
                    models.CharField(
                        choices=[
                            ("Создана", "Создана"),
                            ("Запущена", "Запущена"),
                            ("Завершена", "Завершена"),
                        ],
                        default="Создана",
                        max_length=50,
                        verbose_name="Статус рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="MailingAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_last_mailing",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата и время последней рассылки",
                    ),
                ),
                ("status_mailing", models.BooleanField(verbose_name="Статус рассылки")),
                (
                    "server_response",
                    models.CharField(
                        blank=True, null=True, verbose_name="Ответ сервера"
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылок",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="MessageMailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject_line",
                    models.CharField(max_length=150, verbose_name="Тема письма"),
                ),
                (
                    "body",
                    models.TextField(
                        blank=True, null=True, verbose_name="Текс сообщения"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сообщение рассылки",
                "verbose_name_plural": "Сообщения рассылки",
                "ordering": ("id",),
            },
        ),
    ]
