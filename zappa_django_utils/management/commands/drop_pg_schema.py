from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    """
    Command to drop a schema from a PostgreSQL database.
    """
    help = 'Drops a schema from the PostgreSQL database.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting schema deletion...'))

        dbname = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']

        con = connect(dbname=dbname, user=user, host=host, password=password)

        self.stdout.write(self.style.SUCCESS('Removing schema {schema} from database {dbname}'
                                             .format(schema=settings.SCHEMA, dbname=dbname)))
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = con.cursor()
        cur.execute('DROP SCHEMA {schema} CASCADE;'.format(schema=settings.SCHEMA))
        cur.close()

        con.close()

        self.stdout.write(self.style.SUCCESS('All done.'))
