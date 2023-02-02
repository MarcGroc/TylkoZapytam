#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
import json
from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.client.client_models import Client


class ClientTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client = {
            "client": self.user.id,
            "ip_address": "0.0.0.0",
            "ip_city": "test",
            "country_code": "test",
            "device_type": "test",
            "last_password_change": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "phone_number": "test",
            "questions_asked": 0,
            "calls_scheduled": 0,
            "calls_completed": 0,
        }

    def test_client_ip_address_should_be_valid(self):
        self.assertTrue(self.client["ip_address"].count(".") == 3)
        self.assertTrue(self.client["ip_address"].count(":") == 0)


class ClientAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client_user = {
            "client": self.user.pk,
            "ip_address": "0.0.0.0",
            "ip_city": "test",
            "country_code": "TE",
            "device_type": "test",
            "last_password_change": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "phone_number": "test",
            "questions_asked": 1,
            "calls_scheduled": 1,
            "calls_completed": 1,
        }

    def test_client_api_should_return_201(self):
        response = self.client.post(
            reverse("client-list"),
            json.dumps(self.client_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Client.objects.count(), 1)

    def test_client_api_should_return_400_if_invalid_data(self):
        self.client_user["country_code"] = "test"
        response = self.client.post(
            reverse("client-list"),
            json.dumps(self.client_user),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Client.objects.count(), 0)
