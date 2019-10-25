import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
import django
django.setup()

from faker import Faker
from project.app_2.models import User

faker = Faker()


def populate(n=20):

    for index in range(n):
        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_email = faker.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)


if __name__ == '__main__':
    print('Populating App 2 Script...')
    populate(20)
    print('Populating App 2 Completed.')
