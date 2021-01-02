from subscribe import forms
from smpt.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(data=request.POST)
        subject = 'welcome to brainworks'
        message = 'hello guys we are providing best professional courses'
        recepient = str(sub ['Email'].value())
        send_mail = (subject, EMAIL_HOST_USER, [recepient], message)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form':sub})




