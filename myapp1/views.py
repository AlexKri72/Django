
from django.http import HttpResponse
from random import  randint
import  logging


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

