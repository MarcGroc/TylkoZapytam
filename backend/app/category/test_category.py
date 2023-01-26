import factory
from django.test import TestCase
from django.urls import reverse
from loguru import logger
from rest_framework.test import APITestCase

from .category_controller import CategoryFactory


class CategoryTest(TestCase):
    logger.info(" Running test for app.category Model")

    def setUp(self):
        CategoryFactory.reset_sequence()
        self.category = factory.build(dict, FACTORY_CLASS=CategoryFactory)

    def test_category_instances(self):
        self.assertIsInstance(self.category, dict)
        self.assertIsInstance(self.category["name"], str)


# class CategoryAPITest(APITestCase):
#     logger.info(" Running test for app.category API")
#
#     def setUp(self):
#         CategoryFactory.reset_sequence()
#         self.category = CategoryFactory.build()
#
#     def test_category_api_should_return_201(self):
#         response = self.client.post(
#             reverse("category-list"), data=self.category.__dict__
#         )
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["name"], self.category.name)
