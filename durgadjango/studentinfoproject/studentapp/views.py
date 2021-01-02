from django.shortcuts import render
from studentapp.models import Student

# Create your views here.

def home_page_view(request):
    #students = Student.objects.all()
    #students = Student.objects.filter(marks__lt=35)
    #students = Student.objects.filter(name__startswith='a')
    #students = Student.objects.all().order_by('marks')
    students = Student.objects.all().order_by('-marks')
    return render(request,'testapp/index.html',{'students':students})
