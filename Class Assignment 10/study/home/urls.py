from django.contrib import admin
# from . import category
from django.urls import path
from . import views as home

urlpatterns = [
    path('',home.panel, name='hm'),
    path('login/',home.login, name='lg'),
    path('contact/',home.contact, name='ct'),
    path('register/',home.register, name='rg'),
    path('p_language/',home.p_language, name='pl'),
    path('ur/',home.user, name='usr'),
        
]
