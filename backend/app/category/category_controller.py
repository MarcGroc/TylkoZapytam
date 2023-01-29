import factory
from app.tag.tag_controller import TagFactory

from .category_models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("text", max_nb_chars=100)
    tags = factory.SubFactory(TagFactory)
