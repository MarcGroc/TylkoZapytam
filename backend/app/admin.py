from django.contrib import admin

from .question.question_models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question_text", "answer", "question_date", "answer_date"]
