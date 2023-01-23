from datetime import datetime

from django.test import TestCase
from loguru import logger

from .question_models import Question


class QuestionTest(TestCase):
    logger.info(" Running test for app.question Model")

    @classmethod
    def setUpTestData(cls):

        cls.question = Question.objects.create(
            id=1,
            question_text="test",
            answer="test",
            question_date=datetime.now(),
        )

    def test_question_text(self):
        self.assertEqual(str(self.question.question_text), "test")

    def test_answer(self):
        self.assertEqual(str(self.question.answer), "test")
