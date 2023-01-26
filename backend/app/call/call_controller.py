from datetime import datetime
from random import randrange

import factory
from faker import Faker
from users.client.client_controller import ClientFactory
from users.expert.expert_controller import ExpertFactory

from .call_models import Call

fake = Faker()


class CallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Call

    id = factory.Sequence(lambda n: n + 1)
    call_date = datetime.now()
    call_duration = randrange(10, 30, 5)
    call_type = factory.Iterator(["Incoming", "Outgoing"])
    call_status = factory.Iterator(["Scheduled", "Answered", "Missed"])
    client = factory.SubFactory(ClientFactory)
    expert = factory.SubFactory(ExpertFactory)
