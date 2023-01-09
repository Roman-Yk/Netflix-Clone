from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

MOVIE_TYPE = (
            ('movie', 'movie'),
            ('series', 'series')
            )

GENRES = (
    ('thriller', 'thriller'),
    ('adventure', 'adventure'),
    ('all', 'all'),
    ('fiction', 'fiction'),
    ('action', 'action'),
    ('romance', 'romance'),
    ('horror', 'horror'),
    ('fantasy', 'fantasy'),
    ('historical', 'historical'),
)

TARIFF = (
    ('default','movies'),
    ('plus','plus'),
    ('premium', 'premium'),
)

class Movie(models.Model):
    title = models.CharField(max_length=200,null=True)
    year = models.CharField(max_length=4,null=True)
    age = models.CharField(max_length=3,null=True)
    time = models.CharField(max_length=100,null=True)
    rating = models.CharField(max_length=100,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='movies_img')
    homepage_slider_image = models.ImageField(upload_to='movies_prev_img', null=True)
    genre = models.CharField(max_length=400,null=True)
    movie_type = models.CharField(choices=MOVIE_TYPE, max_length=10, null=True)
    film_url = models.URLField(null= True)

    def __str__(self) -> str:
        return self.title

    def link(self):
        link = 'https://www.youtube.com/embed/' + self.film_url[len('https://www.youtube.com/watch?v='):]
        return link
    
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default = 'profile_pictures/placeholder.png',upload_to='profile_pictures', null = True)
    name = models.CharField(max_length=255, null = True)
    email = models.EmailField(unique=True, null = True)
    password = models.CharField(max_length=255, null = True)
    tariff = models.CharField(choices=TARIFF, null=True, max_length=15)
        
    def __str__(self) -> str:
        return self.name

class UserList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)


class ListedMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    movie_list = models.ForeignKey(UserList, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.movie.title

class Comments(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    text = models.TextField()

