# from django.contrib import admin

# from .models import Choice, Question

# admin.site.register(Question)
# admin.site.register(Choice)
from django.contrib import admin
from .models import Question, Choice


# Inline admin for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # number of blank choice slots


# Custom admin for Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # attach ChoiceInline here


# Register Question with custom admin
admin.site.register(Question, QuestionAdmin)
