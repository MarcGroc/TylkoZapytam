from random import randint

import factory
from django.contrib.auth.models import User
from faker import Faker

from users.client.client_models import Client

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: int(n))
    username = factory.Sequence(lambda n: n)
    password = factory.PostGenerationMethodCall("set_password", "zaq1@WSX")
    email = factory.LazyFunction(fake.email)


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


