#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam

import json
from datetime import datetime

from app.rating.rating_models import Rating
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.client.client_models import Client
from users.expert.expert_models import Expert


class RatingTest(TestCase):
    def setUp(self):
        self.rating = {
            "id": 1,
            "rating": 5,
            "comment": "test",
            "rating_date": datetime.now(),
            "client": 1,
            "expert": 1,
        }

    def test_rating_rating_should_be_in_range_1_to_5(self):
        self.assertGreaterEqual(self.rating["rating"], 1)
        self.assertLessEqual(self.rating["rating"], 5)


class RatingAPI(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.user_client = Client.objects.create(client=self.user)
        self.expert = Expert.objects.create(expert=self.user)
        self.rating = {
            "id": 1,
            "rating": 5,
            "comment": "test",
            "rating_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "client": self.user_client.pk,
            "expert": self.expert.pk,
        }

    def test_rating_api_should_return_201(self):
        response = self.client.post(
            reverse("rating-list"),
            json.dumps(self.rating),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.count(), 1)

    def test_rating_api_should_return_400(self):
        response = self.client.post(
            reverse("rating-list"),
            json.dumps({"rating": 0}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Rating.objects.count(), 0)
