from datetime import datetime
from random import randint

import factory

from .rating_models import Rating


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rating

    rating = randint(1, 5)
    comment = factory.Faker("text", max_nb_chars=1000)
    rating_date = datetime.now()
