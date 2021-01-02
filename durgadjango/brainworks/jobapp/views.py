from django.shortcuts import render
from jobapp.models import PythonStudent, Contacts, About , Courses
from django.http import HttpResponse



# Create your views here.

def home_page(request):
    return render(request,'testapp/homepage.html')

def contact(request):
    contact = Contacts.objects.all()
    return render(request,'testapp/contact.html',{'contact':contact})

def about_us(request):
    about = About.objects.all()
    return render(request,'testapp/aboutus.html',{'about':about})


def courses(request):
    course = Courses.objects.all()
    return render(request,'testapp/course.html',{'course':course})


def python_batch(request):
    student = PythonStudent.objects.all()
    return render(request,'testapp/python.html',{'student':student})
