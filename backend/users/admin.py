from django.contrib import admin

from users.client.client_models import Client
from users.expert.expert_models import Expert


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["client_id", "questions_asked", "calls_scheduled"]


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ["expert_id", "questions_answered", "calls_completed"]
