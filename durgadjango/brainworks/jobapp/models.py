from django.db import models

# Create your models here.

class PythonStudent(models.Model):
    name = models.CharField(max_length=64)
    mob = models.IntegerField()
    email = models.EmailField()
    totalfees = models.FloatField()
    paid = models.FloatField()
    due = models.FloatField()


class Contacts(models.Model):
    Gmail = models.EmailField()
    Linkdin = models.EmailField()
    Yahoo = models.EmailField()
    landline = models.IntegerField()
    mobile = models.IntegerField()
    mobile2 = models.IntegerField()

class About(models.Model):
    info = models.TextField()

class Courses(models.Model):
    python = models.TextField()
    sap= models.TextField()
    matlab = models.TextField()
    dba = models.TextField()
    plsql = models.TextField()
    rpa = models.TextField()
    salesforce = models.TextField()













