from random import randint

import factory
from django.contrib.auth.models import User
from faker import Faker

from .client_models import Client

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    username = factory.LazyFunction(fake.user_name)
    email = factory.LazyFunction(fake.email)
    password = factory.LazyFunction(fake.password)


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    client = factory.SubFactory(UserFactory)
    ip_address = factory.LazyFunction(fake.ipv4)
    ip_city = factory.LazyFunction(fake.city)
    country_code = factory.LazyFunction(fake.country_code)
    device_type = factory.LazyFunction(fake.user_agent)
    last_password_change = factory.LazyFunction(fake.date_time)
    phone_number = factory.LazyFunction(fake.phone_number)
    questions_asked = randint(0, 100)
    calls_scheduled = randint(0, 100)
    calls_completed = randint(0, 100)
