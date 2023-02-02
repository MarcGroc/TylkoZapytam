#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
import json
from datetime import datetime

from app.call.call_models import Call
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.client.client_models import Client
from users.expert.expert_models import Expert


class CallTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user_client = Client.objects.create(client=self.user)
        self.expert = Expert.objects.create(expert=self.user)
        self.call = {
            "id": 1,
            "call_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "call_duration": 10,
            "call_type": "Incoming",
            "call_status": "Scheduled",
            "client": self.user_client.pk,
            "expert": self.expert.pk,
        }

    def test_call_duration_range_should_be_in_range_10_to_30(self):
        self.assertGreaterEqual(self.call["call_duration"], 10)
        self.assertLessEqual(self.call["call_duration"], 30)

    def test_call_type_in_choices(self):
        self.assertIn(self.call["call_type"], ["Incoming", "Outgoing"])

    def test_call_status_in_choices(self):
        self.assertIn(self.call["call_status"], ["Scheduled", "Answered", "Missed"])


class CallAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user_client = Client.objects.create(client=self.user)
        self.expert = Expert.objects.create(expert=self.user)
        self.call = {
            "id": 1,
            "call_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "call_duration": 15,
            "call_type": "Incoming",
            "call_status": "answered",
            "client": self.user_client.pk,
            "expert": self.expert.pk,
        }

    def test_call_api_should_return_201(self):
        response = self.client.post(
            reverse("call-list"), json.dumps(self.call), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Call.objects.count(), 1)

    def test_call_api_should_return_400(self):
        self.call["call_status"] = "wrong"
        response = self.client.post(
            reverse("call-list"), json.dumps(self.call), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Call.objects.count(), 0)
