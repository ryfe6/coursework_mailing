# Generated by Django 4.2 on 2024-05-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="ver_code",
            field=models.CharField(default="010126", max_length=6, verbose_name="Код"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=False, verbose_name="Активность"),
        ),
    ]
