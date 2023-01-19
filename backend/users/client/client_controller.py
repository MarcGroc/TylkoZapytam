import factory
from django.contrib.auth.models import User

from .client_models import Client


class ClientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    user = factory.Sequence(
        lambda n: User.objects.create_user(username="test", password="test")
    )
    ip_address = "0.0.0.0"
    ip_city = "Test City"
    country_code = "TC"
    device_type = "Test Device"
    phone_number = "1234567890"
    questions_asked = 0
    calls_scheduled = 0
    calls_completed = 0

    @staticmethod
    def get_user_dict() -> dict:
        client = {
            "user": User.objects.create_user(username="test"),
            "ip_address": "0.0.0.0",
            "ip_city": "Test City",
            "country_code": "TC",
            "device_type": "Test Device",
            "phone_number": "1234567890",
            "questions_asked": 0,
            "calls_scheduled": 0,
            "calls_completed": 0,
        }

        return client
