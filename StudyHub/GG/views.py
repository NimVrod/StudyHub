from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    sections = Section.objects.all()
    return render(request, 'GG/index.html', {'sections': sections})

def detail(request, section_id):
    section = Section.objects.get(pk=section_id)
    return render(request, 'GG/section.html', {'section': section})