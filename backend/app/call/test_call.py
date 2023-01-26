from datetime import datetime

import factory
from django.test import TestCase
# from django.urls import reverse
from loguru import logger
# from rest_framework.test import APITestCase

from .call_controller import CallFactory


class CallTest(TestCase):
    logger.info(" Running test for app.call Model")

    def setUp(self):
        CallFactory.reset_sequence()
        self.call = factory.build(dict, FACTORY_CLASS=CallFactory)

    def test_call_model_instances(self):
        self.assertIsInstance(self.call, dict)
        self.assertIsInstance(self.call["call_date"], datetime)
        self.assertIsInstance(self.call["call_duration"], int)
        self.assertIsInstance(self.call["call_type"], str)
        self.assertIsInstance(self.call["call_status"], str)

    def test_call_duration_range_should_be_in_range_10_to_30(self):
        self.assertGreaterEqual(self.call["call_duration"], 10)
        self.assertLessEqual(self.call["call_duration"], 30)

    def test_call_date_should_be_less_than_now(self):
        self.assertLess(self.call["call_date"], datetime.now())

    def test_call_type_in_choices(self):
        self.assertIn(self.call["call_type"], ["Incoming", "Outgoing"])

    def test_call_status_in_choices(self):
        self.assertIn(self.call["call_status"], ["Scheduled", "Answered", "Missed"])


# class TestAPICall(APITestCase):
#     logger.info(" Running test for app.call API")
#
#     def setUp(self):
#         CallFactory.reset_sequence()
#         self.call = CallFactory.create()
#         logger.info(self.call)
#
#     def test_call_api_should_return_201(self):
#         response = self.client.post(reverse("call-list"), data=self.call.__dict__)
#         self.assertEqual(response.status_code, 201)
# self.assertEqual(response.data["call_date"], self.call["call_date"])
# self.assertEqual(response.data["call_duration"], self.call["call_duration"])
# self.assertEqual(response.data["call_type"], self.call["call_type"])
# self.assertEqual(response.data["call_status"], self.call["call_status"])
