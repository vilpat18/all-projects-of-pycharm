from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse('first response')

def second_view(request):
    return HttpResponse('second response')

def third_view(request):

    return HttpResponse('IMG_1698.JPG')

def fourth_view(request):
    return HttpResponse('fourth response')
