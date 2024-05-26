import smtplib
from datetime import datetime, timedelta

import pytz
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore

from mailing.models import Mailing, MailingAttempt, MessageMailing


def send_mailing():

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    # mailings = Mailing.objects.filter(status_mailing="Создана")

    quit_mailings = Mailing.objects.filter(
        status_mailing="Запущена", quit_at__lte=current_datetime
    )
    for mailing in quit_mailings:
        mailing.status_mailing = "Завершена"
        mailing.save()

    # Обновление статуса "Создана" на "Запущена" для активных рассылок
    status_mailings = Mailing.objects.filter(
        status_mailing="Создана", next_send_time__lte=current_datetime
    )
    for mailing in status_mailings:
        mailing.status_mailing = "Запущена"
        mailing.save()

    # Получение активных рассылок
    mailings = Mailing.objects.filter(
        status_mailing="Запущена", next_send_time__lte=current_datetime
    )

    for mailing in mailings:
        try:
            send_mail(
                subject=mailing.message.subject_line,
                message=mailing.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.client.all()],
            )

            # Обновление даты следующей отправки
            if mailing.period_mailing == "Раз в день":
                mailing.next_send_time += timedelta(days=1)
            elif mailing.period_mailing == "Раз в неделю":
                mailing.next_send_time += timedelta(weeks=1)
            elif mailing.period_mailing == "Раз в месяц":
                mailing.next_send_time += timedelta(days=30)

            # Сохранение обновленного объекта рассылки
            mailing.save()
            MailingAttempt.objects.create(
                date_last_mailing=current_datetime, status_mailing=True, mailing=mailing
            )
        except smtplib.SMTPException as e:
            MailingAttempt.objects.create(
                date_last_mailing=current_datetime,
                status_mailing=False,
                server_response=e,
                mailing=mailing,
            )


class Command(BaseCommand):

    def handle(self, *args, **options):

        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(
            send_mailing,
            trigger=CronTrigger(minute="*/1"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        try:
            print("Начало рассылки")
            scheduler.start()
        except KeyboardInterrupt:
            print("Завершение рассылки")
            scheduler.shutdown()
