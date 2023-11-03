from django.core.mail import send_mail
from celery import shared_task
from time import sleep

@shared_task
def send_custom_celery_mail(subject, message, sender , receivers):
    # sleep(3)
    send_mail(subject, message, sender , receivers)


def send_custom_ordinary_mail(subject, message, sender , receivers):
    sleep(3)
    send_mail(subject, message, sender , receivers)