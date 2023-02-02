from datetime import datetime
from random import randint

import factory
from users.client.client_controller import ClientFactory
from users.expert.expert_controller import ExpertFactory

from .rating_models import Rating


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    # id = 1
    rating = randint(1, 5)
    comment = "test"
    rating_date = datetime.now()
    client = factory.SubFactory(ClientFactory)
    expert = factory.SubFactory(ExpertFactory)
