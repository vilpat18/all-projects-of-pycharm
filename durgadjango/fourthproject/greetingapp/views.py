from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting(request):
    return HttpResponse('<h1> hello friend have a nice day <h1/>')
