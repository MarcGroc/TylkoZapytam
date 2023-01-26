import factory

from .tag_models import Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"tag{n}")
