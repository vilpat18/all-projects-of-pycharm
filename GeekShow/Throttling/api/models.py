from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class OdiBattingRecord(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    runs = models.IntegerField()
    fifties = models.IntegerField()
    centuries = models.IntegerField()
    double_centuries = models.IntegerField()


class BowlingRecord(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    wickets = models.IntegerField()
    best = models.IntegerField()
    five = models.IntegerField()
