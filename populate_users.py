# These 2 lines allows the code to work in Python 3
import sys
sys.path.append('..')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random

# Python3 alternative should os.environ call wasn't needed ...
# from . import first_app
# from .first_app import AccessRecord, Webpage, Topic

from first_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for entry in range(N):
        fake_email = fakegen.email()
        fake_firstname = fakegen.first_name()
        fake_secondname = fakegen.last_name()
        user = User.objects.get_or_create(email=fake_email, firstname=fake_firstname, secondname=fake_secondname)[0]


if __name__ == "__main__":
    print('Populating script!')
    populate(20)
    print('Populating complete!')
