from datetime import datetime

import factory
from django.contrib.auth.models import User
from django.test import TestCase
from loguru import logger

from .expert_controller import ExpertFactory


class ExpertTest(TestCase):
    logger.info(" Running test for users.expert Model")

    def setUp(self):
        ExpertFactory.reset_sequence()
        self.expert = factory.build(dict, FACTORY_CLASS=ExpertFactory)

    def test_expert_model_instances(self):
        self.assertIsInstance(self.expert, dict)
        self.assertIsInstance(self.expert['user'], User)
        self.assertIsInstance(self.expert['description'], str)
        self.assertIsInstance(self.expert['available'], bool)
        self.assertIsInstance(self.expert['ip_address'], str)
        self.assertIsInstance(self.expert['ip_city'], str)
        self.assertIsInstance(self.expert['country_code'], str)
        self.assertIsInstance(self.expert['device_type'], str)
        self.assertIsInstance(self.expert['last_password_change'], datetime or None)
        self.assertIsInstance(self.expert['phone_number'], str)
        self.assertIsInstance(self.expert['avatar'], str)
        self.assertIsInstance(self.expert['question_price'], int)
        self.assertIsInstance(self.expert['questions_answered'], int)
        self.assertIsInstance(self.expert['call_price'], int)
        self.assertIsInstance(self.expert['calls_scheduled'], int)
        self.assertIsInstance(self.expert['calls_completed'], int)
        self.assertIsInstance(self.expert['category_choices'], str)

    def test_expert_ip_address_should_be_valid(self):
        self.assertTrue(self.expert['ip_address'].count('.') == 3)
        self.assertTrue(self.expert['ip_address'].count(':') == 0)
