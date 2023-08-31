from django.contrib import admin
from . models import user_information, userInfo

# Register your models here.
class user_informationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'batch', 'course',)
admin.site.register(user_information, user_informationAdmin)

class userInfoAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Email', 'phone_number', 'batch', 'texarea', 'password', 're_password','checkbox','payment','django',)
admin.site.register(userInfo, userInfoAdmin)


