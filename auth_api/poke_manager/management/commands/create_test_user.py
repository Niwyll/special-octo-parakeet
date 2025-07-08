from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Run this command to initialize a test user"

    def handle(self, *args, **kwargs):
        self.stdout.write("Initializing test user")
        user, is_created = User.objects.get_or_create(username="testuser", email="foobar@foo.bar")
        if is_created:
            user.set_password("foobar123;")