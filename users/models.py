import random

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}

code = "".join([str(random.randint(0, 9)) for _ in range(6)])


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    avatar = models.ImageField(upload_to="users/", verbose_name="avatar", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="Активность")

    ver_code = models.CharField(default=code, max_length=6, verbose_name="Код")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = (("cancel_user_is_active", "Can cancel user is_active"),)
