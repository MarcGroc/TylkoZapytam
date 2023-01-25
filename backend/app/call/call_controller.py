from random import randrange

import factory
from faker import Faker

from .call_models import Call

fake = Faker()


class CallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Call

    id = factory.Sequence(lambda n: n)
    call_date = factory.LazyFunction(fake.date_time_this_month)
    call_duration = randrange(10, 30, 5)
    call_type = factory.Iterator(["Incoming", "Outgoing"])
    call_status = factory.Iterator(["Scheduled", "Answered", "Missed"])
