from django.contrib.auth.models import User
from django.test import TestCase
from loguru import logger

from .client_models import Client


class ClientTest(TestCase):
    logger.info(" Running test for users.client Model")

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test", password="test")
        cls.client = Client.objects.create(
            user=cls.user,
            ip_address="0.0.0.0",
            ip_city=None,
            country_code="TC",
            device_type="Test Device",
            phone_number="1234567890",
            questions_asked=0,
            calls_scheduled=0,
            calls_completed=0,
        )

    def test_user_username(self):
        self.assertEqual(str(self.user.username), "test")

    def test_client_ip_address(self):
        self.assertEqual(str(self.user.client.ip_address), "0.0.0.0")

    def test_client_device_type(self):
        self.assertEqual(str(self.user.client.device_type), "Test Device")
