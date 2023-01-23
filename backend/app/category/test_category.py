from django.test import TestCase
from loguru import logger

from .category_models import Category, Tag


class CategoryTest(TestCase):
    logger.info(" Running test for app.category Model")

    @classmethod
    def setUpTestData(cls):

        cls.category = Category.objects.create(
            id=1,
            name="test",
            tags=Tag.objects.create(id=1, name="test"),
        )

    def test_category_name(self):
        self.assertEqual(str(self.category.name), "test")

    def test_category_tag(self):
        self.assertEqual(str(self.category.tags), "test")


class TagTest(TestCase):
    logger.info(" Running test for app.tag Model")

    @classmethod
    def setUpTestData(cls):

        cls.tag = Tag.objects.create(id=1, name="test")

    def test_tag_name(self):
        self.assertEqual(str(self.tag.name), "test")
