from django.db import models

# Create your models here.

class user_information(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    batch = models.IntegerField()
    course = models.CharField(max_length=50)
    
