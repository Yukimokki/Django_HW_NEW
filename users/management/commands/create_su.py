from django.core.management import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="noone@skypro.com")
        user.set_password("54321")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
