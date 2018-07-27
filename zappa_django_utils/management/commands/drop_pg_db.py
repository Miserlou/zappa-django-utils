from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Drop the Postgres database completely'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to drop DB..'))

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']

        self.stdout.write(self.style.SUCCESS('Connecting to host..'))
        con = connect(dbname='postgres', user=user, host=host, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.stdout.write(self.style.SUCCESS("Dropping database '{}'".format(dbname)))
        cur = con.cursor()
        cur.execute('DROP DATABASE ' + dbname)
        cur.close()

        con.close()

        self.stdout.write(self.style.SUCCESS('All done!'))
