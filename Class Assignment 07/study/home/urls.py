from django.contrib import admin
# from . import category
from django.urls import path
from . import views as home

urlpatterns = [
    path('panel/',home.panel),
    path('common/',home.variable),
    path('c/',home.variable_data),
    path('ccode/',home.common_code),
        
]
