from random import randint

import factory

from faker import Faker
from users.client.client_controller import UserFactory

from users.expert.expert_models import Expert

fake = Faker()


class ExpertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expert

    expert = factory.SubFactory(UserFactory)
    description = factory.LazyFunction(fake.text)
    available = factory.LazyFunction(fake.boolean)
    ip_address = factory.LazyFunction(fake.ipv4)
    ip_city = factory.LazyFunction(fake.city)
    country_code = factory.LazyFunction(fake.country_code)
    device_type = factory.LazyFunction(fake.user_agent)
    last_password_change = factory.LazyFunction(fake.date_time)
    phone_number = factory.LazyFunction(fake.phone_number)
    question_price = randint(10, 500)
    questions_answered = randint(0, 100)
    call_price = randint(10, 500)
    calls_scheduled = randint(0, 100)
    calls_completed = randint(0, 100)
    # category_choices = factory.SubFactory(CategoryFactory)
    expert_is_verified = factory.LazyFunction(fake.boolean)
