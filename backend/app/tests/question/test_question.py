#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
import json
from datetime import datetime

from app.question.question_models import Question
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.client.client_models import Client
from users.expert.expert_models import Expert


class QuestionTest(TestCase):
    def setUp(self):
        self.question = {
            "id": 1,
            "question_text": "test",
            "answer": "test",
            "question_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "answer_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "1",
            "client": 1,
            "expert": 1,
        }

    def test_question_question_text_should_not_be_empty(self):
        self.assertNotEqual(self.question["question_text"], "")

    def test_question_date_should_be_less_than_answer_date(self):
        self.assertLess(self.question["question_date"], self.question["answer_date"])
        self.assertLessEqual(
            self.question["question_date"], self.question["answer_date"]
        )


class QuestionAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user_client = Client.objects.create(client=self.user)
        self.expert = Expert.objects.create(expert=self.user)
        self.question = {
            "id": 1,
            "question_text": "test",
            "answer": "test",
            "question_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "answer_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "client": self.user_client.pk,
            "expert": self.expert.pk,
        }

    def test_question_api_should_return_201(self):
        response = self.client.post(
            reverse("question-list"),
            json.dumps(self.question),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Question.objects.count(), 1)

    def test_question_api_should_return_400(self):
        response = self.client.post(
            reverse("question-list"),
            json.dumps({"question_text": ""}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Question.objects.count(), 0)
