from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User

import random
import string

class Command(BaseCommand):
    help = 'Creates a default "admin" user'

    def handle(self, *args, **options):

        pw = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

        self.stdout.write(self.style.SUCCESS('Creating new admin user..'))
        User.objects.create_superuser('admin', 'admin@admin.com', pw)
        self.stdout.write(self.style.SUCCESS('Created user "admin", email: "admin@admin.com", password: ' + pw))
        self.stdout.write(self.style.SUCCESS('Log in and change this password immediately!'))
