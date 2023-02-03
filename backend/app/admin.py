from django.contrib import admin
from django.contrib.auth.decorators import login_required
from app.call.call_models import Call
from app.category.category_models import Category
from app.question.question_models import Question
from app.rating.rating_models import Rating
from app.tag.tag_models import Tag

admin.site.login = login_required(admin.site.login)

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
