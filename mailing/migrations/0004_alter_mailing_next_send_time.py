# Generated by Django 4.2 on 2024-05-21 14:00

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_mailing_next_send_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="next_send_time",
            field=models.DateTimeField(
                default=datetime.datetime.now,
                verbose_name="Дата и время отправки рассылки",
            ),
        ),
    ]
