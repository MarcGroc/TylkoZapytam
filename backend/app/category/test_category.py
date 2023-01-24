import factory
from django.test import TestCase
from loguru import logger

from .category_controller import CategoryFactory, TagFactory


class CategoryTest(TestCase):
    logger.info(" Running test for app.category Model")

    def setUp(self):
        TagFactory.reset_sequence()
        CategoryFactory.reset_sequence()
        self.category = factory.build(dict, FACTORY_CLASS=CategoryFactory)

    def test_category_model_instances(self):
        self.assertIsInstance(self.category, dict)
        self.assertIsInstance(self.category['name'], str)
        self.assertIsInstance(self.category['tags'], dict)


# class TagTest(TestCase):
#     logger.info(" Running test for app.tag Model")
#
#     def setUp(self):
#         TagFactory.reset_sequence()
#         self.tag = TagFactory(name="test")
#
#     def test_tag_name(self):
#         self.assertEqual(str(self.tag.name), "test")
