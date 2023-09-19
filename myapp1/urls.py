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
    path('', views.HomeViews.as_view(), name='HomeViews'),
    path('aboutviews/', views.AboutViews.as_view(), name='AboutViews'),
    path('headgame/<int:count>', views.HeadGame.as_view(), name='HeadGame'),
    path('dicegame/<int:count>', views.DiceGame.as_view(), name='DiceGame'),
    path('articles/<int:id_author>', views.AllArticlesViews.as_view(), name='AllArticlesViews'),
    path('article/<int:pk>', views.DetailView.as_view(), name='article'),
    path('client/<int:id_client>', views.ClientOrdersViews.as_view(), name='client'),

]