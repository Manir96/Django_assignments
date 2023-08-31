from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import userCf
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

#Registration form
def userCreafrom(request):
    if request.method == "POST":
        fm = userCf(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = userCf()
    return render (request, 'course/userCreatFm.html', {'form':fm})

#Login form
def login_form_show(request):
    if request.method == 'POST':
        lfrm = AuthenticationForm(request=request, data = request.POST)
        if lfrm.is_valid():
            uname = lfrm.cleaned_data['username']
            upass = lfrm.cleaned_data['password']
            user = authenticate(username =uname, password = upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/course/success')
    else:
        lfrm = AuthenticationForm()        
    return render (request, 'course/login.html', {'form':lfrm})
#login
def slogin(request):
     return render(request, 'course/success.html')
 #logout
def logout_from(request):
    logout(request)
    return render(request, 'course/login.html')

#password_chance
def password_chance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lfrm = PasswordChangeForm(user=request.user, data = request.POST)
            if lfrm.is_valid():
                lfrm.save()
                update_session_auth_hash(request, lfrm.user)
                return HttpResponseRedirect('/course/success')
        else:
            lfrm = PasswordChangeForm(user =request.user)
        return render(request, 'course/pchance.html', {'form':lfrm})
    else:
        return HttpResponseRedirect('/course/login/')
    
#without old password_chance
def without_old_password_chance(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            lfrm = SetPasswordForm(user=request.user, data = request.POST)
            if lfrm.is_valid():
                lfrm.save()
                update_session_auth_hash(request, lfrm.user)
                return HttpResponseRedirect('/course/success')
        else:
            lfrm = SetPasswordForm(user =request.user)
        return render(request, 'course/withoutpchance.html', {'form':lfrm})
    else:
        return HttpResponseRedirect('/course/login/')