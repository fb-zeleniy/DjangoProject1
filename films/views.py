from django.shortcuts import render
from .forms import FilmForm
from .models import *
from django.http import HttpResponse
from .forms import BbForm
from django.shortcuts import render, redirect

def get_all_films(request):
    all_films = Film.objects.all()
    context = {'all_films': all_films}
    return render(request,'films/films.html', context)

def get_film_by_slug(request, slug):
    film = Film.objects.get(slug=slug)
    context={'film': film}
    return render(request, 'film/film.html', context)

def get_film_by_id(request, pk):
    film = Film.obkects.get(pk=pk)
    context = {'film' : film}
    return render(request, 'film/film.html', context)

def regular_films(request):
    all_films = Film.objects.all()
    context = {'all_films' : all_films}
    return render(request, 'films/films.html', context)

def add_and_save_film(request):
    if request.method=="POST":
        filmform=FilmForm(request.POST)
        if filmform.is_valid():
            filmform.save()
            return HttpResponse(reversed("films:all"))
        else:
            context = {'form': filmform}
            return render(request, 'films/add_film.html', context)
    else:
            filmform = FilmForm()
            context = {'form': filmform}
            return render(request, 'films/add_film.html', context)


def index(request):
    response= HttpResponse("Здесь будет",content_type="text/plain; charset=utf-8")
    response.write('главная')
    response.writelines(('страница','сайта'))
    response["keywords"]="Pythob Django"
    return response


def create_bb(request):
    if request.method == 'POST':
        form = BbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bb_list')
    else:
        form = BbForm()

    return render(request, 'create_bb.html', {'form': form})