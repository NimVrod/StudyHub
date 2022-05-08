from django.contrib import admin
from .models import *


# Register your models here.

class RIPINLINE(admin.TabularInline):
    model = RIP


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [RIPINLINE]


admin.site.register(Section, SectionAdmin)
