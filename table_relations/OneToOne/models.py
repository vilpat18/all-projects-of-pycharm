from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)


class Page(models.Model):
    creator = models.OneToOneField(Creator,on_delete=models.CASCADE)
    page_name = models.CharField(max_length=24)
    page_type = models.CharField(max_length=256)
    page_publish = models.DateField()