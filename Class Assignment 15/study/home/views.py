from django.shortcuts import render
from . models import user_information, userInfo
from .forms import userRegistration
from django.http import HttpResponseRedirect


# Create your views here.
def panel(request):
    return render(request,'common_code/home.html')


def login(request):
    return render(request,'common_code/courses.html')

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
       
        if frm.is_valid():
            F_Name = frm.cleaned_data['First_Name']
            L_Name = frm.cleaned_data['Last_Name']
            email = frm.cleaned_data['Email']
            p_number = frm.cleaned_data['phone_number']
            bat = frm.cleaned_data['batch']
            text = frm.cleaned_data['texarea']
            passw = frm.cleaned_data['password']
            re_pass = frm.cleaned_data['re_password']
            c_box = frm.cleaned_data['checkbox']
            pay = frm.cleaned_data['payment']
            dj = frm.cleaned_data['django']
            
            data = userInfo( First_Name = F_Name, Last_Name = L_Name, Email = email,phone_number = p_number, batch = bat, texarea = text, password = passw, re_password = re_pass, checkbox = c_box, payment = pay, django = dj, ) 
            data.save()  
            return HttpResponseRedirect('/successfully/')
    else:
        frm = userRegistration()
        print('Execute GET')
    return render(request,'common_code/froms.html', {'froms':frm})

def success(request):
    return render(request,'common_code/submit.html',)




# def formsuccess(request):
#     if request.method == 'POST':
#         frms = userRegistration(request.POST)
#         # print(frm)
#         print('Execute POST')
#         print(frms.cleaned_data)
#         print('Email:', frms.cleaned_data['Email'])
#         print('First_Name:', frms.cleaned_data['First_Name'])
#         print('password:', frms.cleaned_data['password'])
#         print('re_password:', frms.cleaned_data['re_password'])
#         if frms.is_valid():
#             print('Valid Data')
#             print(frms.cleaned_data)
#             return HttpResponseRedirect('/success/')
#     else:
#         frms = userRegistration()
#         print('Execute GET')
#     return render(request,'common_code/froms.html',{'success':frms})

