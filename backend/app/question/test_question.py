from datetime import datetime

import factory
from django.test import TestCase

# from django.urls import reverse

from .question_controller import QuestionFactory

# from rest_framework.test import APITestCase


class QuestionTest(TestCase):

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


# TODO: Tests for API calls with APITestCase
