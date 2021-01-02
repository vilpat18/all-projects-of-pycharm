from django.db import models

# Create your models here.

class Teams(models.Model):
    Mumbai = models.CharField(max_length=100)
    Delhi = models.CharField(max_length=100)
    Banglore = models.CharField(max_length=100)

