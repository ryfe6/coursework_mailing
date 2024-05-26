from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from mailing.models import NULLABLE


class BlogView(models.Model):
    heading = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    photo = models.ImageField(upload_to="blogs/", verbose_name="Фотография", **NULLABLE)
    content = models.TextField(verbose_name="содержимое")
    created_at = models.DateField(verbose_name="Дата создания")
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name="количество просмотров")
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE
    )

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
