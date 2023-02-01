from datetime import datetime

import factory
from django.test import TestCase

# from django.urls import reverse

from .call_controller import CallFactory

# from rest_framework.test import APITestCase


class CallTest(TestCase):

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


# TODO: Tests for API calls with APITestCase


class CallAPITest(TestCase):
    pass
