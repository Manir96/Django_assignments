from django.contrib import admin
from . models import teacher, Student, Subject

# Register your models here.

@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display = ('registration', 'teacher_name', 'user',)
    
#many to one 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'subject', 'student_reg', 'user',)

#many to many
@admin.register(Subject)
class SubjecttAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_cod',)