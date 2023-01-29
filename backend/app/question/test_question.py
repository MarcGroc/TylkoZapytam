from datetime import datetime

import factory
from django.test import TestCase
# from django.urls import reverse
from loguru import logger
# from rest_framework.test import APITestCase

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


# class QuestionAPITest(APITestCase):
#     logger.info(" Running test for app.question API")
#
#     def setUp(self):
#         QuestionFactory.reset_sequence()
#         self.question = QuestionFactory.create()
#
#     def test_question_api_should_return_201(self):
#         response = self.client.post(
#             reverse("question-list"), data=self.question.__dict__
#         )
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data["question_text"], self.question.question_text)
#         self.assertEqual(response.data["answer"], self.question.answer)
