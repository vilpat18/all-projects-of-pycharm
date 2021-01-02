from django.shortcuts import render
from rest_framework.views import APIView
from restapp3.models import Players
from restapp3.serializers import PlayersSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView , CreateAPIView,RetrieveAPIView,\
    UpdateAPIView,DestroyAPIView,ListCreateAPIView,\
    RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

#class PlayerListAPIView(APIView):
#   def get(self,request,format=None):
#        qs= Players.objects.all()
#        serializer = PlayersSerializer(qs,many=True) serialiser convrt qs to python native data type (dict)
#        return Response(serializer.data)

# class PlayerListAPIView(ListAPIView):
#     # queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
#     def get_queryset(self):
#         qs = Players.objects.all()
#         name = self.request.GET.get('pname')
#         if name is not None:
#             qs = qs.filter(pname__icontains=name)
#         return qs


# class PlayerListAPIView(ListAPIView): to get all fields from the table in list
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
#

# class PlayerCreateAPIView(CreateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

# class PlayerRetriveAPIView(RetrieveAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
#
# class PlayerUpdateAPIView(UpdateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

#
# class PlayerDestroyAPIView(DestroyAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer


# class PlayerRetriveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

# class PlayerRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

# class PlayerListCreateAPIView(ListCreateAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer
#
#
# class PlayerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Players.objects.all()
#     serializer_class = PlayersSerializer

from rest_framework import mixins
from rest_framework import generics
class PlayerListCreateModelMixin(mixins.CreateModelMixin,ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class PlayerRetriveUpdateDestroyModelMixin(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)










