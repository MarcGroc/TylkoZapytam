from django.contrib.auth.models import User
from django.test import TestCase
from loguru import logger

from .expert_models import Expert


class ClientTest(TestCase):
    logger.info(" Running test for users.expert Model")

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="test", password="test")
        cls.expert = Expert.objects.create(
            user=cls.user,
            description="Test Description",
            available=False,
            working_hours=["00:00", "00:00", "00:00"],
            ip_address="0.0.0.0",
            ip_city=None,
            country_code="TC",
            device_type="Test Device",
            last_password_change=None,
            phone_number="1234567890",
            avatar=None,
            question_price=0,
            questions_answered=0,
            call_price=0,
            calls_scheduled=0,
            calls_completed=0,
            category_choices=["Test Category"],
        )

    def test_user_username(self):
        self.assertEqual(str(self.user.username), "test")

    def test_client_ip_address(self):
        self.assertEqual(str(self.user.expert.ip_address), "0.0.0.0")

    def test_client_device_type(self):
        self.assertEqual(str(self.user.expert.device_type), "Test Device")

    def test_expert_description(self):
        self.assertEqual(str(self.user.expert.description), "Test Description")

    def test_expert_available(self):
        self.assertEqual(str(self.user.expert.available), "False")

    def test_expert_call_price(self):
        self.assertEqual(int(self.user.expert.call_price), 0)
