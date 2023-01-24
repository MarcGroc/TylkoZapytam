import factory

from datetime import datetime

from .tag_models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f"tag{n}")
    created = datetime.now()
