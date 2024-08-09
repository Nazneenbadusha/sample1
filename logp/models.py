from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField(default='default_email@example.com')
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)




    
