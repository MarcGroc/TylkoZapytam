import factory
from django.test import TestCase
# from django.urls import reverse
from loguru import logger
# from rest_framework.test import APITestCase

from .tag_controller import TagFactory


class TagTest(TestCase):
    logger.info(" Running test for app.tag Model")

    def setUp(self):
        TagFactory.reset_sequence()
        self.tag = factory.build(dict, FACTORY_CLASS=TagFactory)

    def test_tag_model_instances(self):
        self.assertIsInstance(self.tag, dict)
        self.assertIsInstance(self.tag["name"], str)
        # self.assertIsInstance(self.tag["created"], datetime)

    def test_tag_name_length_should_be_in_range_3_to_30(self):
        self.assertGreaterEqual(len(self.tag["name"]), 3)
        self.assertLessEqual(len(self.tag["name"]), 30)

    # def test_tag_created_date_should_be_less_than_now(self):
    #     self.assertLess(self.tag["created"], datetime.now())


# class TagAPITest(APITestCase):
#     logger.info(" Running test for app.tag API")
#
#     def setUp(self):
#         TagFactory.reset_sequence()
#         self.tag = TagFactory.build()
#
#     def test_tag_api_should_return_201(self):
#         response = self.client.post(reverse("tag-list"), data=self.tag.__dict__)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["name"], self.tag.name)
