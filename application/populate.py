import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
import django
django.setup()

import random
from faker import Faker
from project.app_1.models import AccessRecord, Topic, WebPage

faker = Faker()

topics = ['Software Engineering', 'Sport']


def add_topic():
    topic = Topic.objects.get_or_create(name=random.choice(topics))[0]
    topic.save()

    return topic


def populate(n=5):

    for index in range(n):
        topic = add_topic()
        fake_url = faker.url()
        fake_date = faker.date()
        fake_name = faker.domain_name()

        web_page = WebPage.objects.get_or_create(topic=topic, name=fake_name, url=fake_url)[0]
        access_record = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)


if __name__ == '__main__':
    print('Populating Script...')
    populate(20)
    print('Populating Completed.')
