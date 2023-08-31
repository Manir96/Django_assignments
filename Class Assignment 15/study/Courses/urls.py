from django.contrib import admin
# from . import category
from django.urls import path
from . import views as Course

urlpatterns = [
    path('courses/',Course.userCreafrom, name='registration'),
    path('lgin/',Course.login_form_show, name='login'),
    path('success/',Course.slogin,),
    path('logout/',Course.logout_from, name='logout'),
    path('pchanc/',Course.password_chance, name='passwordchance'),
    path('without/',Course.without_old_password_chance, name='passwordoldchance'),
    path('classblog/',Course.first_class.as_view()),
    path('template_view/',Course.first_template.as_view()),
    path('redirect_view/',Course.RedirectView.as_view(url='course/logout')),
    path('extranal/',Course.extranal_url.as_view()),
          
]
