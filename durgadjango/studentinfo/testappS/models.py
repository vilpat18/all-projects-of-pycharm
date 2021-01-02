from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=64)
    dob=models.charfield(max_length=12)
    marks = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.TextField()
