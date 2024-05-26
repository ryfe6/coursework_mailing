from django.core.management import BaseCommand
from django.db import connection

from blog.models import BlogView


class Command(BaseCommand):
    """Класс для работы с БД приложения catalog"""

    def handle(self, *args, **options):
        """Функция очищает БД и записывает новые данные из фикстуры."""
        BlogView.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("""ALTER SEQUENCE blog_blogview_id_seq RESTART WITH 1""")
        self.stdout.write(self.style.SUCCESS("Данные о рассылках успешно удалены"))
