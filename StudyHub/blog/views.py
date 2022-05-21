from django.shortcuts import render
from .models import Blog, Gallery
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', {"blogs": blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    gallery = Gallery.objects.filter(blog=blog)
    return render(request, 'blog/detail.html', {"blog": blog, "gallery": gallery})
