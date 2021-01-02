from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_morning(request):
    return HttpResponse('<h1> hello friend good morning <h1/>')

def hello_afternoon(request):
    return HttpResponse('<h1> hello friend good afternoon <h1/>')

def hello_evening(request):
    return HttpResponse('<h1> hello friend good evening <h1/>')
