from django.contrib import admin
import nested_admin

from .models import quiz, pytanie, odpowiedz


# Register your models here.

class Choice(nested_admin.NestedStackedInline):
    model=odpowiedz
    extra = 1

class Question(nested_admin.NestedStackedInline):
    model = pytanie
    extra = 2
    inlines=[
        Choice
    ]

class Quiz(nested_admin.NestedModelAdmin):
    fieldsets = [
        (None, {'fields': ["name"]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [
        Question
    ]


admin.site.register(quiz, Quiz)
