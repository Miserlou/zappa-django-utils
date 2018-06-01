from django.core.management.base import BaseCommand
from django.db import connection, DatabaseError
from django.conf import settings


class Command(BaseCommand):
    """
    This command performs a vacuum on the S3SQLite database.
    It is good to do this occasionally to keep the SQLite database stored
    on S3 as small and unfragmented as possible. It is recommended to be
    run after deleting data.
    """
    help = 'Performs a vacuum command on a S3 stored SQLite database to minimize size and fragmentation.'

    def handle(self, *args, **options):
        if settings.DATABASES['default']['ENGINE'] != "zappa_django_utils.db.backends.s3sqlite":
            raise DatabaseError('This command is only for the s3sqlite Django DB engine.')
        else:
            self.stdout.write(self.style.SUCCESS('Starting database VACUUM...'))
            cursor = connection.cursor()
            cursor.execute('VACUUM;')
            cursor.close()
            self.stdout.write(self.style.SUCCESS('VACUUM complete.'))
