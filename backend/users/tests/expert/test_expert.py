#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
# import json
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
# from django.urls import reverse
from rest_framework.test import APITestCase
# from users.expert.expert_models import Expert


class ExpertTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.expert = {
            "expert": self.user.pk,
            "description": "test",
            "available": True,
            "ip_address": "0.0.0.0",
            "ip_city": "TE",
            "country_code": "TE",
            "device_type": "test",
            "last_password_change": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "phone_number": "test",
            "avatar": "test.jpg",
            "question_price": 1,
            "qusetions_answered": 1,
            "call_price": 1,
            "calls_scheduled": 1,
            "calls_completed": 1,
            "expert_is_verified": True,
        }

    def test_expert_ip_address_should_be_valid(self):
        self.assertTrue(self.expert["ip_address"].count(".") == 3)
        self.assertTrue(self.expert["ip_address"].count(":") == 0)


class ExpertAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.expert = {
            "expert": self.user.pk,
            "description": "test",
            "available": True,
            "ip_address": "0.0.0.0",
            "ip_city": "TE",
            "country_code": "TE",
            "device_type": "test",
            "last_password_change": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "phone_number": "test",
            "avatar": "test.jpg",
            "question_price": 1,
            "qusetions_answered": 1,
            "call_price": 1,
            "calls_scheduled": 1,
            "calls_completed": 1,
            "expert_is_verified": True,
        }

    # def test_expert_api_should_return_201(self):
    #     print(self.expert)
    #     response = self.client.post(
    #         reverse("expert-list"), json.dumps(self.expert), content_type="application/json"
    #     )
    #     print(response.data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Expert.objects.count(), 1)
