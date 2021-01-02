from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse


class UserSerializer(object):
    pass


@api_view(['GET'])
def user_details(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)


class User1Serializer(object):
    pass


@csrf_exempt
def user_detaa(request):
    if request.method == "GET":
        users1 = User.objects.all()
        serializer = User1Serializer(users1,many=True)
        return JsonResponse(serializer.data)


from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)