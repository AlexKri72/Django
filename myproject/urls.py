from django.contrib import admin
from django.urls import path, include
from lection03.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp1.urls')),
    path('lection03/', include('lection03.urls')),
    path('', index),
    path('myapp1/', include('myapp1.urls')),
    path('lection04/', include('lection04.urls')),

    ]
