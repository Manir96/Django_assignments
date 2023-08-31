from django.contrib import admin
from . models import user_information

# Register your models here.
class user_informationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'batch', 'course',)
admin.site.register(user_information, user_informationAdmin)

