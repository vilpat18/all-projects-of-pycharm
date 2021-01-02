from django.shortcuts import render
import datetime

# Create your views here.

def time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h<12:
        msg = "hello friend!!!! good morning"
    elif h<16:
        msg = 'hello supriya !! good afternoon'
    elif h<21:
        msg = 'hello friend !! good evening'
    else:
        msg = 'hello friend !! good night'

    my_dict = {'date':date,'msg': msg}
    return render(request,'testapp/results.html',my_dict)