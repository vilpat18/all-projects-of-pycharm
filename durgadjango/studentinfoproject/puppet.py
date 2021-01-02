import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
import django
django.setup()
from studentapp.models import Student
from faker import Faker
from random import *
fake = Faker()

def phonenumber():
    d1=randint(6,9)
    num =''+ str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphonenumber=phonenumber()
        faddress=fake.address()
        student_record=Student.object.get(roll_no=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
populate(30)




