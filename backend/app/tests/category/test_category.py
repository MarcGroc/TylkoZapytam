#  Copyright (c) 2023.  Marc Groc
#  https://github.com/MarcGroc/TylkoZapytam
import json

from app.category.category_models import Category
from app.tag.tag_models import Tag
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class CategoryTest(TestCase):
    def setUp(self):
        self.tags = Tag.objects.create(name="test")
        self.category = {"id": 1, "name": "test", "tags": self.tags.id}

    def test_category_instances(self):
        self.assertIsInstance(self.category, dict)
        self.assertIsInstance(self.category["name"], str)


class CategoryAPITest(APITestCase):
    def setUp(self):
        self.tags = Tag.objects.create(name="test")
        self.category = {"id": 1, "name": "test", "tags": self.tags.id}

    def test_category_api_should_return_201(self):
        response = self.client.post(
            reverse("category-list"),
            json.dumps(self.category),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)

    def test_category_api_should_return_400_if_invalid_data(self):
        response = self.client.post(
            reverse("category-list"),
            json.dumps({"name": ""}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Category.objects.count(), 0)

    def test_category_api_should_return_400_if_category_exists(self):
        response = self.client.post(
            reverse("category-list"),
            json.dumps(self.category),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)
        response = self.client.post(
            reverse("category-list"),
            json.dumps(self.category),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
