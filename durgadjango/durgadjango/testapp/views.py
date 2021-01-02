from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>this is django application<h1/>' )
def indian_team(request):
    return HttpResponse('<h1> indian cricket team captain is rohit <h1/>')