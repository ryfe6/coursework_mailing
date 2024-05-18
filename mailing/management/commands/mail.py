from django.core.mail import send_mail
from django.core.management import BaseCommand

import smtplib
from datetime import datetime, timedelta
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F

from mailing.models import Mailing, MessageMailing, MailingAttempt


class Command(BaseCommand):

    def handle(self, *args, **options):
        period_mailing = ["Раз в день", "Раз в неделю", "Раз в месяц"]
        zone = pytz.timezone(settings.TIME_ZONE)
        current_datetime = datetime.now(zone)
        mailings = Mailing.objects.filter(status_mailing="Запущена").filter(create_date=current_datetime)
        for mailing in mailings:
            status = False
            server_response = "Нет ответа"
            send_mail(
                subject=MessageMailing.subject_line,
                message=MessageMailing.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()],
                fail_silently=False
            )