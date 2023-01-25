import factory

from .category_models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("text", max_nb_chars=100)
    tags = factory.Faker("text", max_nb_chars=100)
