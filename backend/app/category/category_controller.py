import factory

from datetime import datetime

from .category_models import Category, Tag


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f"tag{n}")
    created = datetime.now()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"category{n}")
    tags = factory.RelatedFactory(TagFactory, "category")
    created = datetime.now()
