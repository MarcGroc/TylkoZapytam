from datetime import datetime

import factory
from django.test import TestCase
from loguru import logger

from .client_controller import ClientFactory


class ClientTest(TestCase):
    logger.info(" Running test for users.client Model")

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
