import factory
from django.test import TestCase

# from django.urls import reverse
from loguru import logger

from .category_controller import CategoryFactory

# from rest_framework.test import APITestCase


class CategoryTest(TestCase):
    logger.info(" Running test for app.category Model")

    def setUp(self):
        CategoryFactory.reset_sequence()
        self.category = factory.build(dict, FACTORY_CLASS=CategoryFactory)

    def test_category_instances(self):
        self.assertIsInstance(self.category, dict)
        self.assertIsInstance(self.category["name"], str)


# TODO: Tests for API calls with APITestCase
