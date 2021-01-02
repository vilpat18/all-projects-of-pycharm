from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    username = models.CharField(max_length=10)
    mobile = models.BigIntegerField()
    password = models.TextField(null=False)
    image = models.ImageField(null=False)
    confirm_password = models.TextField(null=False)
    recovery_email = models.EmailField(null=False)

    def __str__(self):
        return self.username