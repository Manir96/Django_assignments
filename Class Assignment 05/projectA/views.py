from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'welcome.html')

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index")