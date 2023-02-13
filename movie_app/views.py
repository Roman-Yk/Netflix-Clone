from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
import random

import json
# Create your views here.

def index(request):
    return render(request, 'movie_app/index.html')
    

@login_required(login_url='accounts:login')
def homepage(request):
    movies = Movie.objects.all()
    title_movie = random.choice(movies)
    context = {'movies': movies, 'title_movie': title_movie}
    return render(request, 'movie_app/homepage.html', context)
 
 
@login_required(login_url='accounts:login')
def series_page(request):
    #filter by series
    series = Movie.objects.filter(movie_type = 'series')
    context = {'movies': series, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/series.html', context)
 
 
@login_required(login_url='accounts:login')
def movies_page(request, genre='all'):
    #check which genre was choosen
    if genre == 'all':
        movies = Movie.objects.filter(movie_type = 'movie')
    else:
        #filter by genre
        movies = Movie.objects.filter(genre__contains=genre, movie_type = 'movie')
    context = {'movies': movies, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/movies.html', context)
 
 
@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
def genred_series(request, genre):
    #check which genre was choosen
    if genre == 'all':
        series = Movie.objects.filter(movie_type = 'series')
    else:
        #filter by genre
        series = Movie.objects.filter(genre__contains=genre, movie_type = 'series')
    context = {'series': series, 'genres': sorted(GENRES)}
    return render(request, 'movie_app/series.html', context)
 
 
@login_required(login_url='accounts:login')
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


@login_required(login_url='accounts:login')
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




@login_required(login_url='accounts:login')
def profile(request):
    # get customer
    customer = request.user.customer
    if request.method == "POST":
        # get sended data
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            # check if aany files were sended
            # if were, then change profile picture
            if 'document' in request.FILES:
                customer.profile_pic = request.FILES['document']
            # update customer name
            customer.name = form.cleaned_data.get('name')
            # save changes
            customer.save()
    else:
        form = CustomerForm(instance=customer)
    context = {'form':form}
    return render(request, 'movie_app/profile.html', context)



@login_required(login_url='accounts:login')
def tariff(request):
    # check request method
    if request.method == "POST":
        form = TariffForm(request.POST)
        # check if form is valid
        if form.is_valid():
            # get customer
            customer = request.user.customer
            # change customer tariff
            customer.tariff = form.cleaned_data['tariff']
            # save changes
            customer.save()
    else:
        form = TariffForm()
        
    context = {'tariffs':TARIFF, 'form': form}
    return render(request, 'movie_app/tariff.html', context)