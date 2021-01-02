from django.db import models


# Create your models here.

class Student(models.Model):
    rollnumber = models.IntegerField()
    name = models.CharField(max_length=64)
    dob = models.CharField(max_length=64)
    marks = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()