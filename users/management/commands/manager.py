from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Скрипт для создания группы модератора в админке."""

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name="manager")
        moderator_group.permissions.add(Permission.objects.get(codename='view_clientservice'))
        moderator_group.permissions.add(Permission.objects.get(codename='cancel_mailing_status_mailing'))
        moderator_group.permissions.add(Permission.objects.get(codename='view_mailing'))
        moderator_group.permissions.add(Permission.objects.get(codename='view_messagemailing'))
        moderator_group.permissions.add(Permission.objects.get(codename='cancel_user_is_active'))
        moderator_group.permissions.add(Permission.objects.get(codename='view_user'))

        # Введите _email пользователя, который будет наделен правами модератора
        _email = "manager@sky.pro"
        if _email == "_":
            print("Группа manager создана")
        else:
            user = User.objects.get(email=_email)
            user.groups.add(moderator_group)
            print("Группа manager создана и пользователь успешно добавлен")
