from datetime import datetime

import factory
from django.test import TestCase
from loguru import logger

from .question_controller import QuestionFactory


class QuestionTest(TestCase):
    logger.info(" Running test for app.question Model")

    def setUp(self):
        QuestionFactory.reset_sequence()
        self.question = factory.build(dict, FACTORY_CLASS=QuestionFactory)

    def test_question_instances(self):
        self.assertIsInstance(self.question, dict)
        self.assertIsInstance(self.question["question_text"], str)
        self.assertIsInstance(self.question["answer"], str)
        self.assertIsInstance(self.question["question_date"], datetime)
        self.assertIsInstance(self.question["answer_date"], datetime)

    def test_question_question_date_should_be_less_than_now(self):
        self.assertLess(self.question["question_date"], datetime.now())
