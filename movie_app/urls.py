from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('filmpage/<int:filmId>/', views.single_filmpage, name='filmpage'),
    path('series/', views.series_page, name='series_page'),
    path('series/<str:genre>/', views.genred_series, name='genred_series'),
    path('movies/<str:genre>/', views.movies_page, name='movies_page'),
    path('mylist/<str:genre>/', views.user_movie_list, name='mylist'),
    path('add_to_userlist/', views.add_to_userlist, name='add_to_userlist'),
     path('profile/', views.profile, name='profile')
]


