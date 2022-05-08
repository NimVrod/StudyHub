from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.forms import ModelForm, widgets
import datetime

# Create your views here.

def index(request):
    sections = Section.objects.all()
    return render(request, 'GG/index.html', {'sections': sections})


def detail(request, section_id):
    section = Section.objects.get(pk=section_id)
    users = RIP.objects.filter(section=section)
    return render(request, 'GG/section.html', {'section': section, 'users': users})


def user_info(request, user_id):
    user = RIP.objects.get(pk=user_id)
    j = {
        'name': user.name,
        'date': user.date,
        'description': user.description,
    }
    return JsonResponse(j)


class UserForm(ModelForm):
    class Meta:
        model = RIP
        fields = ['name', 'date', 'description', 'section']
        widgets = {'date': widgets.DateInput(attrs={'type': 'date', 'value': datetime.date.today()})}


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        return render(request, 'GG/add_user.html', {'form': UserForm()})
