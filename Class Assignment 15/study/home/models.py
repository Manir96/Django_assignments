from django.db import models

# Create your models here.

class user_information(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    batch = models.IntegerField()
    course = models.CharField(max_length=50)
    
class userInfo(models.Model):
    First_Name = models.CharField(max_length=300)
    Last_Name = models.CharField(max_length=300)
    Email = models.EmailField(max_length=300)
    phone_number = models.CharField(max_length=12)
    batch = models.IntegerField()
    texarea = models.CharField(max_length=500)
    password = models.CharField(max_length=40)
    re_password = models.CharField(max_length=40)
    checkbox = models.CharField(max_length=50)
    payment = models.DecimalField(max_digits=6, decimal_places=2)
    django = models.BooleanField(max_length=30)
    
