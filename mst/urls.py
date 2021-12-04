from django.contrib import admin
from django.urls import path
from . import code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', code.standart, name='hhome'),
    path('rev/', code.reverse, name='reverse'),
]
