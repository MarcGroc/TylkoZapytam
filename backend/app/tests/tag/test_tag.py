#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
import json

from app.tag.tag_models import Tag
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class TagTest(TestCase):
    def setUp(self):
        self.tag = {"id": 1, "name": "test"}

    def test_tag_model_instances(self):
        self.assertIsInstance(self.tag["name"], str)

    def test_tag_name_length_should_be_in_range_3_to_30(self):
        self.assertGreaterEqual(len(self.tag["name"]), 3)
        self.assertLessEqual(len(self.tag["name"]), 30)


class TagAPITest(APITestCase):
    def setUp(self):
        self.tag = {"id": 1, "name": "test"}

    def test_tag_api_should_return_201_if_created(self):
        response = self.client.post(
            reverse("tag-list"), json.dumps(self.tag), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 1)

    def test_tag_api_should_return_400_if_invalid(self):
        response = self.client.post(
            reverse("tag-list"), json.dumps({}), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Tag.objects.count(), 0)

    def test_tag_api_should_return_400_if_tag_already_exists(self):
        response = self.client.post(
            reverse("tag-list"), json.dumps(self.tag), content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tag.objects.count(), 1)
        response = self.client.post(
            reverse("tag-list"), json.dumps(self.tag), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
