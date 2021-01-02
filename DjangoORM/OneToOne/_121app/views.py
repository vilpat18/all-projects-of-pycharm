from django.shortcuts import render

# Create your views here.
from .models import Place,Waiter,Restaurant
from .serialisers import PlaceSerializer,WaiterSerializer,RestaurantSerializer
from rest_framework import viewsets


class PlaceApiView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class WaiterApiView(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer


class RestaurantApiView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer