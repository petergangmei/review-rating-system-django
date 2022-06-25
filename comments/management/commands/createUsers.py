from django.core.management.base import BaseCommand
from faker import Faker
from comments.models import Review
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = "Command information!"
    

    def handle(sef, *args, **kwargs):
        f = Faker()
        for _ in range(10):
            # d = f.unique
            User.objects.create(author=usr, name=f.name(), stars=random.randint(1,5),comment=f.text())
            print("Created!")