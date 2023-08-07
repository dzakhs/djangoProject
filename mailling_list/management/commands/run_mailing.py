import time

from django.core.management.base import BaseCommand
import schedule

from mailling_list.models import Client


def test_schedule():
    print('Старт рассылки')



class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule.every(3).seconds.do(test_schedule)
        while True:
            schedule.run_pending()
            time.sleep(1)