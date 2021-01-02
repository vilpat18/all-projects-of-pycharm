from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=10)
    phone = models.BigIntegerField()
    address = models.TextField()
    password = models.CharField(max_length=10)
    renter_password = models.CharField(max_length=10)

