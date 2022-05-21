from django.contrib import admin
from .models import Blog, Gallery
# Register your models here.

class GalleryAdmin(admin.TabularInline):
    model=Gallery

class BlogAdmin(admin.ModelAdmin):
    model=Blog
    inlines=[GalleryAdmin]

admin.site.register(Blog, BlogAdmin)
