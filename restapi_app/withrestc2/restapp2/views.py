from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapp2.serializers import NameSerializer


class TestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        fruits = ['mango', 'banana', 'apple', 'grapes']
        return Response({'msg': 'hello world', 'fruits': fruits})

    # def post(self,request,*args,**kwargs):
    #        serializer = NameSerializer(data=request.data)
    #        if serializer.is_valid():
    #            name = serializer.data.get('name')
    #            msg = 'hello {},good morning'.format(name)
    #            return Response({'msg':msg})
    #        else:
    #            return Response(serializer.errors,status=400)

    def put(self,request,*args,**kwargs):
        return Response({'msg':'this response from put method of APIView'})

    def patch(self, request, *args, **kwargs):
        return Response({'msg': 'this response from patch method of APIView'})

    def delete(self, request, *args, **kwargs):
        return Response({'msg': 'this response from delete method of APIView'})

# class Test(APIView):



'''from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request,*args,**kwargs):
        sports = ['cricket','football','hocky','baseball']
        return Response({'msg':'outdoor games','sports':sports})
    # def create(self,request):
    #   serializer = NameSerializer(data=request.data)
    # if serializer.is_valid():
    #   name = serializer.data.get('name')
    #  msg = 'hello {},good morning'.format(name)
    #  return Response({'msg':msg})
    # else:
    #  return Response(serializer.errors,status=400)
    def retrive(self,request,pk=None):
        return Response({'msg':'this is respns from retrive method'})

    def update(self, request, pk=None):
        return Response({'msg': 'this is respns from retrive method'})

    def partial_update(self, request, pk=None):
        return Response({'msg': 'this is respns from retrive method'})

    def destroy(self, request, pk=None):
        return Response({'msg': 'this is respns from retrive method'})'''






