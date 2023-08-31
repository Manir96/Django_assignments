from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import userCf



# Create your views here.

def userCreafrom(request):
    if request.method == "POST":
        fm = userCf(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = userCf()
    return render (request, 'course/userCreatFm.html', {'form':fm})