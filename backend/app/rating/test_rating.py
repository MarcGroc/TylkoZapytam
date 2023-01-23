from datetime import datetime

from django.test import TestCase
from loguru import logger

from .rating_models import Rating


class RatingTest(TestCase):
    logger.info(" Running test for app.rating Model")

    @classmethod
    def setUpTestData(cls):

        cls.rating = Rating.objects.create(
            id=1,
            rating=5,
            comment="test",
            rating_date=datetime.now(),
        )

    def test_rating(self):
        self.assertEqual(self.rating.rating, 5)

    def test_comment(self):
        self.assertEqual(str(self.rating.comment), "test")

    def test_rating_invalid(self):
        self.assertNotEqual(self.rating.rating, 0)
