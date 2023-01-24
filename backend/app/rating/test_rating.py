from datetime import datetime

import factory
from django.test import TestCase
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
        self.assertIsInstance(self.rating["user_id"], dict)

    def test_rating_rating_should_be_in_range_1_to_5(self):
        self.assertGreaterEqual(self.rating["rating"], 1)
        self.assertLessEqual(self.rating["rating"], 5)

    def test_rating_rating_date_should_be_less_than_now(self):
        self.assertLess(self.rating["rating_date"], datetime.now())
