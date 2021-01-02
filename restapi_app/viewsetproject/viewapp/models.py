from django.db import models


class Players(models.Model):
    pno = models.IntegerField()
    pname = models.CharField(max_length=64)
    pruns = models.IntegerField()
    pteam = models.CharField(max_length=64)
