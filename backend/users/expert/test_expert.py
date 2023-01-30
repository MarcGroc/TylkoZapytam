from datetime import datetime

import factory
from django.test import TestCase

# from django.urls import reverse
from loguru import logger

from .expert_controller import ExpertFactory

# from rest_framework.test import APITestCase
# from users.client.client_controller import UserFactory


class ExpertTest(TestCase):
    logger.info(" Running test for users.expert Model")

    def setUp(self):
        ExpertFactory.reset_sequence()
        self.expert = factory.build(dict, FACTORY_CLASS=ExpertFactory)

    def test_expert_model_instances(self):
        self.assertIsInstance(self.expert, dict)
        self.assertIsInstance(self.expert["description"], str)
        self.assertIsInstance(self.expert["available"], bool)
        self.assertIsInstance(self.expert["ip_address"], str)
        self.assertIsInstance(self.expert["ip_city"], str)
        self.assertIsInstance(self.expert["country_code"], str)
        self.assertIsInstance(self.expert["device_type"], str)
        self.assertIsInstance(self.expert["last_password_change"], datetime or None)
        self.assertIsInstance(self.expert["phone_number"], str)
        self.assertIsInstance(self.expert["question_price"], int)
        self.assertIsInstance(self.expert["questions_answered"], int)
        self.assertIsInstance(self.expert["call_price"], int)
        self.assertIsInstance(self.expert["calls_scheduled"], int)
        self.assertIsInstance(self.expert["calls_completed"], int)

    def test_expert_ip_address_should_be_valid(self):
        self.assertTrue(self.expert["ip_address"].count(".") == 3)
        self.assertTrue(self.expert["ip_address"].count(":") == 0)


# class ExpertAPITest(APITestCase):
#     logger.info(" Running test for users.expert API")
#
#     def setUp(self):
#         UserFactory.reset_sequence()
#         ExpertFactory.reset_sequence()
#         self.expert = factory.build(dict, FACTORY_CLASS=ExpertFactory)
#         self.expert["expert"] = UserFactory().id
#     def test_expert_api_should_return_201(self):
#         response = self.client.post(reverse("expert-list"), data=self.expert)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["description"], self.expert["description"])
#         self.assertEqual(response.data["available"], self.expert["available"])
#         self.assertEqual(response.data["ip_address"], self.expert["ip_address"])
#         self.assertEqual(response.data["ip_city"], self.expert["ip_city"])
#         self.assertEqual(response.data["country_code"], self.expert["country_code"])
#         self.assertEqual(response.data["device_type"], self.expert["device_type"])
#         self.assertEqual(response.data["last_password_change"], self.expert["last_password_change"])
#         self.assertEqual(response.data["phone_number"], self.expert["phone_number"])
#         # self.assertEqual(response.data["avatar"], self.expert["avatar"])
#         self.assertEqual(response.data["question_price"], self.expert["question_price"])
#         self.assertEqual(response.data["questions_answered"], self.expert["questions_answered"])
#         self.assertEqual(response.data["call_price"], self.expert["call_price"])
#         self.assertEqual(response.data["calls_scheduled"], self.expert["calls_scheduled"])
#         self.assertEqual(response.data["calls_completed"], self.expert["calls_completed"])
