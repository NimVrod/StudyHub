import django.http
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import quiz, pytanie, odpowiedz
from .forms import QuizForm, PytanieForm, OdpowiedzForm
from django.forms import inlineformset_factory


# Create your views here.
def index(request):
    quizes_list = quiz.objects.order_by("-pub_date")[:10]
    viewd_list = quiz.objects.order_by("-views")[:10]
    return render(request, 'quizes/quiz_index.html', {"last": quizes_list, "viewed": viewd_list})


def detail(request, quiz_id):
    try:
        detailed = quiz.objects.get(pk=quiz_id)
    except quiz.DoesNotExist:
        raise Http404("No quiz with that id exists.")
    # return HttpResponse(detailed.name)
    detailed.views += 1
    detailed.save()
    return render(request, 'quizes/quiz_detail.html', {"quiz": detailed})


def add(request):
    if request.is_ajax():
        print("AJAX")
    else:
        print("Not ajax")
        return render(request, 'quizes/quiz_add.html')
