
from django.http import HttpResponse
from random import  randint
import  logging
from django.views.generic import TemplateView,DetailView
from myapp1.models import GameModel, Post, Autor, Order,Product, Client


logger = logging.getLogger(__name__)
def heads(request):
    res= 'HEADS' if  randint(0,1) else 'TAIL'
    logger.info(f'{res=}')
    return HttpResponse(res)

def cube(request):
    res=str(randint(1,6))
    logger.info(f'{res=}')
    return HttpResponse(res)

def rand_num(request):
    res=str(randint(1,100))
    logger.info(f'{res=}')
    return HttpResponse(res)

def home(request):
    html='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Главная страница</h1>
</body>
</html>'''
    return HttpResponse(html)

def about(request):
    html='''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Обо мне</h1>
</body>
</html>'''
    return HttpResponse(html)


class GameView(TemplateView):
    template_name = 'myapp1/game.html'

class HeadGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result=[('TAILS','HEADS') [randint(0,1)]for i in  range(self.kwargs['count'])]
        context['results']=result
        context['title']='Игра в орла и решку'
        return context
class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = [[randint(1, 6)] for i in range(self.kwargs['count'])]
        context['results'] = result
        context['title'] = 'Игральный кубик'
        return context


def index(request):
    result = ('TAIL', 'HEADS')[randint(0, 1)]
    game = GameModel(result=result)
    game.save()
    return HttpResponse(f'{game}')

def last_game(request):
    last=GameModel().return_last(5)
    return HttpResponse('<br>'+ str(i) for i in last)

from  myapp1.models import Autor
def autor(request):
    res= Autor.objects.all()
    return  HttpResponse(res)


class HomeViews(TemplateView):
    template_name = 'myapp1/base.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Гланая'
        return context

class AboutViews(TemplateView):
    template_name = 'myapp1/about.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        return context

class AllArticlesViews(TemplateView):
    template_name = 'myapp1/articles.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        author= Autor.objects.get(pk=self.kwargs['id_author'])
        articles = Post.objects.filter(autor=author).all()
        context['articles'] = articles
        return context

class DetailArticle(DetailView):
    model = Post
    template_name = 'myapp1/detail.html'
    context_object_name = 'article'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views+=1
        obj.save()
        return obj

class ClientOrdersViews(TemplateView):
    template_name = 'myapp1/orders.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        client = Client.objects.get(pk=self.kwargs['id_client'])
        orders= Order.objects.filter(client=client).all()
        #products = Product.objects.filter(order=order).all()
        context['orders'] = orders
        context['title'] = 'Список товаров'
        return context