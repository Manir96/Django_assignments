from django.shortcuts import render
from . models import user_information
from .forms import userRegistration
from django.http import HttpResponseRedirect

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

def show_form(request):
    if request.method == 'POST':
        frm = userRegistration(request.POST)
        # print(frm)
        print('Execute POST')
        print(frm.cleaned_data)
        print('Email:', frm.cleaned_data['Email'])
        print('First_Name:', frm.cleaned_data['First_Name'])
        print('password:', frm.cleaned_data['password'])
        print('re_password:', frm.cleaned_data['re_password'])
        if frm.is_valid():
            print('Valid Data')
            print(frm.cleaned_data)
            return HttpResponseRedirect('/successfully/')
    else:
        frm = userRegistration()
        print('Execute GET')
    return render(request,'common_code/froms.html', {'form':frm},)

def success(request):
    return render(request,'common_code/submit.html',)