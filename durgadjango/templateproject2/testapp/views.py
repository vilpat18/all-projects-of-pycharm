from django.shortcuts import render
import datetime

# Create your views here.

def greeting(request):
    date = datetime.datetime.now()
    hr = int(date.strftime('%H'))
    msg = 'hello friend !!! '
    if hr<12:
        msg = msg + ' good morning'
    elif hr < 16:
        msg = msg + ' good afternoon'
    elif hr < 21:
        msg = msg +' good evening'
    else:
        msg = msg + ' good night'
    response = render(request,'testapp/results1.html',{'m':msg,'d':date})
    return response