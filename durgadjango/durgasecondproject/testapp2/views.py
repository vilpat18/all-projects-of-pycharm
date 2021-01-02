from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def date_time_now(request):
    date =datetime.now()
    s = '<h1> the curent date and time of server is :' + str(date)+ '<h1/>'
    return HttpResponse(s)
