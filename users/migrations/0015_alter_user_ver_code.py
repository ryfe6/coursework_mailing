# Generated by Django 4.2 on 2024-05-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_alter_user_ver_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ver_code",
            field=models.CharField(default="221378", max_length=6, verbose_name="Код"),
        ),
    ]
