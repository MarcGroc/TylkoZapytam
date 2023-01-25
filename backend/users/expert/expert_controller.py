from random import randint

import factory
from django.contrib.auth.models import User
from faker import Faker

from .expert_models import Expert

fake = Faker()


class ExpertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expert

    user = factory.Sequence(
        lambda n: User.objects.create_user(username="test", password="test")
    )
    description = factory.LazyFunction(fake.text)
    available = factory.LazyFunction(fake.boolean)
    ip_address = factory.LazyFunction(fake.ipv4)
    ip_city = factory.LazyFunction(fake.city)
    country_code = factory.LazyFunction(fake.country_code)
    device_type = factory.LazyFunction(fake.user_agent)
    last_password_change = factory.LazyFunction(fake.date_time)
    phone_number = factory.LazyFunction(fake.phone_number)
    avatar = factory.LazyFunction(fake.image_url)
    question_price = randint(10, 500)
    questions_answered = randint(0, 100)
    call_price = randint(10, 500)
    calls_scheduled = randint(0, 100)
    calls_completed = randint(0, 100)
    category_choices = factory.Iterator(
        ["Health", "Finance", "Technology", "Education"]
    )
    is_verified = factory.LazyFunction(fake.boolean)
