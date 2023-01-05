from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.http import JsonResponse
from .forms import *

import json
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'movie_app/index.html')
    else:
        return redirect("homepage")


def homepage(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movie_app/homepage.html', context)
 
def series_page(request):
    #filter by series
    series = Movie.objects.filter(movie_type = 'series')
    context = {'series': series, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/series.html', context)
 
def movies_page(request, genre='all'):
    #check which genre was choosen
    if genre == 'all':
        movies = Movie.objects.filter(movie_type = 'movie')
    else:
        #filter by genre
        movies = Movie.objects.filter(genre__contains=genre, movie_type = 'movie')
    context = {'movies': movies, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/movies.html', context)
 
def single_filmpage(request, filmId):
    addible = True
    customer = request.user.customer
    film = Movie.objects.get(id=filmId)
    # getting userlist to create remove from list functionality
    user_list, created = UserList.objects.get_or_create(customer=customer)
    listed_films = user_list.listedmovie_set.all()
    if listed_films.filter(movie=film).exists():
        addible = False
    context = {'film': film, 'addible': addible}
    return render(request, 'movie_app/film_page.html', context)


def genred_series(request, genre):
    #check which genre was choosen
    if genre == 'all':
        series = Movie.objects.filter(movie_type = 'series')
    else:
        #filter by genre
        series = Movie.objects.filter(genre__contains=genre, movie_type = 'series')
    context = {'series': series, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/series.html', context)
 
 
#User movie list 
def user_movie_list(request, genre):
    customer = request.user.customer
    user_list,created = UserList.objects.get_or_create(customer=customer)
    if genre == 'all':
        movie_list = user_list.listedmovie_set.all()
    else:
        #filter by genre
        movie_list = user_list.listedmovie_set.filter(movie__genre__contains=genre)
    context = {'list':movie_list, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/my_list.html', context)


def add_to_userlist(request):
    # get user
    customer = request.user.customer
    # get data from request body
    data = json.loads(request.body)
    # get movie using movie id from data
    movie = Movie.objects.get(id=data['movieId'])
    # get or create userlist using customer 
    user_list, created = UserList.objects.get_or_create(customer=customer)
    # check action
    if data['action'] == 'add':
        # get listed movie using userlist and movie 
        listed_movie = ListedMovie.objects.get_or_create(movie_list=user_list, movie=movie)
        addible = False
    elif data['action'] == 'remove':
        # remove listed movie using userlist and movie 
        listed_movie = ListedMovie.objects.get(movie_list=user_list, movie=movie).delete()
        addible = True
    # return JsonResponse
    return JsonResponse({'addible': addible}, safe=False)





def profile(request):
    customer = request.user.customer
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
    else:
        form = CustomerForm()
    context = {'form':form}
    return render(request, 'movie_app/profile.html', context)