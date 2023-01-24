from django.apps import AppConfig
from django.db import connection, OperationalError
from loguru import logger


class ApConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    def ready(self):
        import app.signals
        logger.info("Ensure database connection")
        try:
            connection.ensure_connection()
            logger.info("Database connection ensured")
        except OperationalError:
            logger.error("Database connection failed")