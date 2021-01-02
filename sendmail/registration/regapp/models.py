from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=8)
    password2 = models.CharField(max_length=8)
    mobile = models.IntegerField(unique=True)
    recovery_email = models.EmailField(unique=True)





