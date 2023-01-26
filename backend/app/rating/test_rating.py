from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from loguru import logger

from .rating_controller import RatingFactory


class RatingTest(TestCase):
    logger.info(" Running test for app.rating Model")

    def setUp(self):
        RatingFactory.reset_sequence()
        self.rating = factory.build(dict, FACTORY_CLASS=RatingFactory)

    def test_rating_model_instances(self):
        self.assertIsInstance(self.rating, dict)
        self.assertIsInstance(self.rating["rating"], int)
        self.assertIsInstance(self.rating["comment"], str)
        self.assertIsInstance(self.rating["rating_date"], datetime)

    def test_rating_rating_should_be_in_range_1_to_5(self):
        self.assertGreaterEqual(self.rating["rating"], 1)
        self.assertLessEqual(self.rating["rating"], 5)

    def test_rating_rating_date_should_be_less_than_now(self):
        self.assertLess(self.rating["rating_date"], datetime.now())


class RatingAPI(TestCase):
    logger.info(" Running test for app.rating API")

    def setUp(self):
        RatingFactory.reset_sequence()
        self.rating = RatingFactory.create()

    def test_rating_api_should_return_201(self):
        response = self.client.post(reverse("rating-list"), data=self.rating.__dict__)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["rating"], self.rating.rating)
        self.assertEqual(response.data["comment"], self.rating.comment)
