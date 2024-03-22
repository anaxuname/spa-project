from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@example.com",
            full_name="Admin",
            is_superuser=True,
            is_staff=True,
            password="1example",
        )

        # user.set_password("1example")
        user.save()
