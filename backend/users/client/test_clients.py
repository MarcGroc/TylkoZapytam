from datetime import datetime

import factory
from django.test import TestCase

# from django.urls import reverse

from .client_controller import ClientFactory

# from rest_framework.test import APIClient, APITestCase


class ClientTest(TestCase):

    def setUp(self):
        ClientFactory.reset_sequence()
        self.client = factory.build(dict, FACTORY_CLASS=ClientFactory)

    def test_client_model_instances(self):
        self.assertIsInstance(self.client, dict)
        self.assertIsInstance(self.client["ip_address"], str)
        self.assertIsInstance(self.client["ip_city"], str)
        self.assertIsInstance(self.client["country_code"], str)
        self.assertIsInstance(self.client["device_type"], str)
        self.assertIsInstance(self.client["last_password_change"], datetime or None)
        self.assertIsInstance(self.client["phone_number"], str)
        self.assertIsInstance(self.client["questions_asked"], int)
        self.assertIsInstance(self.client["calls_scheduled"], int)
        self.assertIsInstance(self.client["calls_completed"], int)

    def test_client_ip_address_should_be_valid(self):
        self.assertTrue(self.client["ip_address"].count(".") == 3)
        self.assertTrue(self.client["ip_address"].count(":") == 0)


# class ClientAPITest(APITestCase):
#
#     def setUp(self):
#         UserFactory.reset_sequence()
#         ClientFactory.reset_sequence()
#         self.user = factory.build(dict, FACTORY_CLASS=ClientFactory)
#         self.user["client"] = UserFactory().id
#     def test_client_api_should_return_201(self):
#         response = self.client.post(reverse("client-list"), data=self.user)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["ip_address"], self.user["ip_address"])
#         self.assertEqual(response.data["ip_city"], self.user["ip_city"])
#         self.assertEqual(response.data["country_code"], self.user["country_code"])
#         self.assertEqual(response.data["device_type"], self.user["device_type"])
#         self.assertEqual(response.data["phone_number"], self.user["phone_number"])
#         self.assertEqual(response.data["questions_asked"], self.user["questions_asked"])
#         self.assertEqual(response.data["calls_scheduled"], self.user["calls_scheduled"])
#         self.assertEqual(response.data["calls_completed"], self.user["calls_completed"])
