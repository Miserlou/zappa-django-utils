from django.core.management.base import BaseCommand
from django.conf import settings

import MySQLdb as db


class Command(BaseCommand):
    help = "Create a database from settings file prior to migrations."

    def add_arguments(self, parser):
        parser.add_argument(
            '--user',
            dest='user',
            help='Username to be used to create database',
        )
        parser.add_argument(
            '--password',
            dest='password',
            help='Password for the mysql user.',
        )
        parser.add_argument(
            '--db-name',
            dest='db_name',
            help='Name of the database if it is different from the one defined in settings',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting db creation'))

        dbname = options.get('db_name') or settings.DATABASES['default']['NAME']
        user = options.get('user') or settings.DATABASES['default']['USER']
        password = options.get('password') or settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']

        con = db.connect(user=user, host=host, password=password)
        cur = con.cursor()
        cur.execute(f'CREATE DATABASE {dbname}')
        cur.execute(f'ALTER DATABASE `{dbname}` CHARACTER SET utf8')
        cur.close()
        con.close()

        self.stdout.write(self.style.SUCCESS('All Done'))
