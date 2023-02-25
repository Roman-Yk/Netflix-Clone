from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('filmpage/<int:filmId>/', views.single_filmpage, name='filmpage'),
    path('series/<str:genre>/', views.series_page, name='series_page'),
    path('movies/<str:genre>/', views.movies_page, name='movies_page'),
    path("movies_search/<str:genre>/", views.searched_movies, name="search"),
    path('mylist/<str:genre>/', views.user_movie_list, name='mylist'),
    path('add_to_userlist/', views.add_to_userlist, name='add_to_userlist'),
    path('profile/', views.profile, name='profile'),
    path('choose_tariff/', views.tariff, name='tariff'),
]


