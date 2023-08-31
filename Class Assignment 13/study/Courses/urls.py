from django.contrib import admin
# from . import category
from django.urls import path
from . import views as Course

urlpatterns = [
    path('courses/',Course.userCreafrom, name='cr'),
      
]
