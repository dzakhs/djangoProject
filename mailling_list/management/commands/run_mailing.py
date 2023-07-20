import time

from django.core.management.base import BaseCommand
import schedule

def test_schedule():
    print('Старт рассылки')

class Command(BaseCommand):
    def handle(self, *args, **options):
        schedule.every(3).seconds.do(test_schedule)
        while True:
            schedule.run_pending()
            time.sleep(1)