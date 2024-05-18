from django.apps import AppConfig
from time import sleep
from django.core.management import call_command


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        sleep(2)
        call_command("start_aps_mailing")
