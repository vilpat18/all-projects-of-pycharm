from django.shortcuts import render
from testappS.models import Student

# Create your views here.

def home_page(request):
    students = Student.objects.all()
    return render(request,'testapp/index.html',{'students':students})

