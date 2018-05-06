import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
# Import settings
django.setup()

from faker import Faker
from second_app.models import Name

def make_data(N=3):
    fake_obj = Faker()
    for data in range(N):
        fake_name = Name.objects.get_or_create(name=fake_obj.first_name(), last=fake_obj.last_name(), email=fake_obj.email())[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    make_data(10)
    print('Populating Complete')
