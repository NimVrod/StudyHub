from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import quiz


# Create your views here.
def index(request):
    quizes_list = quiz.objects.all()[:20]
    return render(request, 'files/quiz_index.html', {"list": quizes_list})


def detail(request, quiz_id):
    try:
        detailed = quiz.objects.get(pk=quiz_id)
    except quiz.DoesNotExist:
        raise Http404("No quiz with that id exists.")
    #return HttpResponse(detailed.name)
    return render(request, 'files/quiz_detail.html', {"quiz": detailed})
