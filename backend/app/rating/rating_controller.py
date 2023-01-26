from datetime import datetime
from random import randint

import factory
from users.client.client_controller import ClientFactory
from users.expert.expert_controller import ExpertFactory

from .rating_models import Rating


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    id = factory.Sequence(lambda n: n)
    rating = randint(1, 5)
    comment = factory.Faker("text", max_nb_chars=300)
    rating_date = datetime.now()
    client = factory.SubFactory(ClientFactory)
    expert = factory.SubFactory(ExpertFactory)
