from django.shortcuts import render
from . models import user_information

# Create your views here.
def panel(request):
    return render(request,'common_code/home.html')


def login(request):
    return render(request,'common_code/login.html')

def contact(request):
    return render(request,'common_code/contact.html')

def register(request):
    return render(request,'common_code/register.html',)

def p_language(request):
    return render(request,'common_code/p_language.html',)

def user(request):
    detals = user_information.objects.all()
    return render(request,'common_code/user.html', {'user':detals})