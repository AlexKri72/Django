from django.urls import path
from . import views


urlpatterns = [
    path('heads/', views.heads, name='heads'),
    path('cube/', views.cube, name='cube'),
    path('number/', views.rand_num, name='rand_num'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('game/', views.last_game, name='last_game'),
    path('autor/', views.autor, name='autor'),
]