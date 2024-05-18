from mailing.management.commands.aps_mailing import start, send_mailing
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        start()
        send_mailing()

