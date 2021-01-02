from django.db import models

# Create your models here.
class Players(models.Model):
    pno = models.IntegerField()
    pname = models.CharField(max_length=64)
    pruns = models.IntegerField()
    pteam = models.CharField(max_length=64)
