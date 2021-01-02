from django.shortcuts import render
import datetime

# Create your views here.

def template_view(request):
    dt = datetime.datetime.now()
    my_dict = {'date':dt}
    return render(request,'Ttestapp/results.html',my_dict)

def shopping_view(request):
    return render(request,'Ttestapp/shopping.html')