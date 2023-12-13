"""
Django command to wait for database to  be available
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for database...')
        # self.stdout.write is how you print in Django
        db_connected = False
        while not db_connected:
            try:
                self.check(databases=['default'])
                # self.check is a function that Django provides that will check
                # if the database is available. If it is,
                # it will return True. If it's not, it will raise an exception.
                db_connected = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
