import factory
from django.contrib.auth.models import User
from faker import Faker

from .client_models import Client

fake = Faker()


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    ip_address = factory.LazyFunction(fake.ipv4)
    ip_city = factory.LazyFunction(fake.city)
    country_code = factory.LazyFunction(fake.country_code)
    device_type = factory.LazyFunction(fake.user_agent)
    last_password_change = factory.LazyFunction(fake.date_time)
    phone_number = factory.LazyFunction(fake.phone_number)
    questions_asked = factory.LazyFunction(fake.random_int)
    calls_scheduled = factory.LazyFunction(fake.random_int)
    calls_completed = factory.LazyFunction(fake.random_int)
