from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Wait for database"

    def handle(self, *args, **options):
        while True:
            try:
                connections["default"].cursor()
                self.stdout.write(self.style.SUCCESS("Database available"))
                break
            except OperationalError:
                self.stdout.write("Waiting for database...")
                time.sleep(1)