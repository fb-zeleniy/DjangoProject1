from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    s = "Список объявлений\n\n\n\n\n"
    for b in Bb.objects.all():
        s += b.title + "\n" + b.content + "\n\n\n"
    return HttpResponse(s, content_type="text/plain; charset=utf-8")


def index_html(request):
    bbs = Bb.objects.all()
    rubrics=Rubric.objects.all()
    context={"bbs":bbs, "rubrics":rubrics}
    return render(request, 'index.html', context)



def index2(request):
    return HttpResponse("Python Django")


def index3(request):
    return HttpResponse("HomeWork")


def detail(request, pk):
    rubric=Rubric.objects.get(pk=pk)
    context={"rubric":rubric}
    return render(request, 'detail.html')

def detail_bb(request, pk):
    bb=Bb.objects.get(pk=pk)
    context={"bb":bb}
    return render(request, 'detail_bb.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')