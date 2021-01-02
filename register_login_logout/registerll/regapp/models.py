from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your models here.
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


class Login(models.Model):
    username =models.ForeignKey(Register,on_delete=models.CASCADE,)
    password = models.TextField(Register)

    def __str__(self):
        return self.username


@receiver(reset_password_token_created)
def password_reset_token_created(sender,instance,reset_password_token,**kwargs):
    email_plan_text_msg = "{}?token={}".format(reverse('password_reset:reset-password-request'),reset_password_token.key)

    send_mail(
        "password reset for {title}".format(title='www.google.com'),
        email_plan_text_msg,'vilasbpatil9993@gmail.com',[reset_password_token.user.mail]
        )

class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class StudentInfo(models.Model):
    mobile = models.BigIntegerField()
    email = models.EmailField()
    student_info = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.student_info