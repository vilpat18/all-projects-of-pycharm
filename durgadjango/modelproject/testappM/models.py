from django.db import models

# Create your models here.
class Employee(models.Model):
    e_no = models.IntegerField()
    e_name =models.CharField(max_length=64)
    e_salary = models.FloatField()
    e_add = models.CharField(max_length=64)



