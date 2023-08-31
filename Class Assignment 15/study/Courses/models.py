from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50)
    registration = models.IntegerField(max_length=30)
    
#many to one relationship
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_reg = models.IntegerField(max_length=30)
    subject = models.CharField(max_length=30)

#many to many relationship
class Subject(models.Model):
    user = models.ManyToManyField(User,)
    subject_name = models.CharField(max_length=50)
    subject_cod = models.IntegerField(max_length=30)
    

