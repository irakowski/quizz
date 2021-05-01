from django.contrib import admin
from . import models

# Register your models here.'
class QuestionInlineModel(admin.TabularInline):
    model = models.Question
    fields = ['text']

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'text', 
        'is_correct'
    ]

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    inlines=[QuestionInlineModel]


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'text', 
        'category'
    ]
    list_display = [
        'text'
    ]
    inlines = [
        AnswerInlineModel
    ]
