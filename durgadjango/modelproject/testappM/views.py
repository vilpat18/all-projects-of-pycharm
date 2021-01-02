from django.shortcuts import render
from testappM.models import Employee
import datetime

# Create your views here.

def table_view(request):
    date = datetime.datetime.now()
    employees = Employee.objects.all()
    return render(request,'testapp/table.html',{'date':date,'employees':employees})

