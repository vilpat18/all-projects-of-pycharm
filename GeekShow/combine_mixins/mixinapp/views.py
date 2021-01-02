from django.shortcuts import render

# Create your views here.
from .models import Teams
from .serialisers import TeamSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,\
                                    UpdateModelMixin,DestroyModelMixin


class TeamListCreateMixinAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class TeamRetrieveUpdateDestroyMixinAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)