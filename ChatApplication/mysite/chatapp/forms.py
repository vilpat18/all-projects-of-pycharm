from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register(request):
    form = UserCreationForm
    return render(request,'chatapp/register.html',{'form':form})
