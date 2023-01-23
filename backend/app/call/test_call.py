from datetime import datetime

from django.test import TestCase
from loguru import logger

from .call_models import Call


class CallTest(TestCase):
    logger.info(" Running test for app.call Model")

    @classmethod
    def setUpTestData(cls):

        cls.call = Call.objects.create(
            id=1,
            call_date=datetime.now(),
            call_duration=1,
            call_type="test",
            call_status="test",
        )

    def test_call_type(self):
        self.assertEqual(str(self.call.call_type), "test")

    def test_call_status(self):
        self.assertEqual(str(self.call.call_status), "test")
