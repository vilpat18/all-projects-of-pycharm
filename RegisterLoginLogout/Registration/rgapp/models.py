from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(null=False)
    mobile = models.BigIntegerField()
    password = models.TextField(null=False)
    image = models.ImageField(null=False)
    confirm_password = models.TextField(null=False)
    recovery_email = models.EmailField(null=False)

    def __str__(self):
        return self.email


class login(models.Model):
    username = models.ForeignKey(Register,on_delete= models.CASCADE,)
    password = models.TextField(Register)


    def __str__(self):
        return self.username
