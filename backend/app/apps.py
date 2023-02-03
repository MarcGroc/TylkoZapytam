from django.apps import AppConfig
from django.db import OperationalError, connection


class ApConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    def ready(self):
        import app.signals

        try:
            connection.ensure_connection()
        except OperationalError:
            raise OperationalError("Database connection failed")
