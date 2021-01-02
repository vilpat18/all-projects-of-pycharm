from django.db import models

# Create your models here.
class Contact_info(models.Model):
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=256)

class Employee(models.Model):
    e_name = models.CharField(max_length=256)
    e_salary = models.IntegerField()
    e_contact_info = models.ForeignKey(Contact_info,on_delete=models.CASCADE)

    def __str__(self):
        return self.e_name


class Manager(models.Model):
    m_name = models.CharField(max_length=256)
    m_salary = models.IntegerField()
    m_contact_info = models.ForeignKey(Contact_info,on_delete=models.CASCADE)

    def __str__(self):
        return self.m_name