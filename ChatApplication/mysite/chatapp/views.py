from django.shortcuts import render

# Create your views here.

from chatapp.models import Registration


def home_page(request):
    return render(request,'chatapp/homepage.html')

def Register(request):
    first_name = request.POST('first_name')
    middle_name = request.POST('middle_name')
    last_name = request.POST('last_name')
    gender = request.POST('gender')
    phone = request.POST('phone')
    address = request.POST('address')
    password = request.POST('password')
    renter_password = request.POST('renter_password')
    register = Registration(first_name=first_name,middle_name=middle_name,last_name=last_name,gender=gender,phone=phone,address=address, password=password,renter_password=renter_password)
    register.save()
    return render(request,register.html)

