from datetime import datetime

import factory
from django.test import TestCase
from loguru import logger

from .call_controller import CallFactory


class CallTest(TestCase):
    logger.info(" Running test for app.call Model")

    def setUp(self):
        CallFactory.reset_sequence()
        self.call = factory.build(dict, FACTORY_CLASS=CallFactory)

    def test_call_model_instances(self):
        self.assertIsInstance(self.call, dict)
        self.assertIsInstance(self.call['call_date'], datetime)
        self.assertIsInstance(self.call['call_duration'], int)
        self.assertIsInstance(self.call['call_type'], str)
        self.assertIsInstance(self.call['call_status'], str)

    def test_call_duration_range_should_be_in_range_10_to_30(self):
        self.assertGreaterEqual(self.call['call_duration'], 10)
        self.assertLessEqual(self.call['call_duration'], 30)

    def test_call_type_in_choices(self):
        self.assertIn(self.call['call_type'], ['Incoming', 'Outgoing'])

    def test_call_status_in_choices(self):
        self.assertIn(self.call['call_status'], ['Scheduled', 'Answered', 'Missed'])
