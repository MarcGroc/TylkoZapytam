from datetime import datetime
from random import randint

import factory
from app.rating.rating_models import Rating
from users.client.client_controller import ClientFactory
from users.expert.expert_controller import ExpertFactory


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    id = 1
    rating = randint(1, 5)
    comment = "test"
    rating_date = datetime.now()
    client = factory.SubFactory(ClientFactory)
    expert = factory.SubFactory(ExpertFactory)
