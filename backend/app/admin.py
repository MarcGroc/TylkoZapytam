from django.contrib import admin

from .call.call_models import Call
from .category.category_models import Category, Tag
from .question.question_models import Question
from .rating.rating_models import Rating


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question_text", "answer", "question_date", "answer_date"]


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ["id", "call_date", "call_duration", "call_type", "call_status"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["id", "rating", "comment", "rating_date"]
