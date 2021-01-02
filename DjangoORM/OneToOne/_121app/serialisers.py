from .models import Restaurant,Waiter,Place
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
    # fields = ['id','name','address']
        fields = ('__all__')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('__all__')
    # fields = ['place','serves_burger','serves_pizza']


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        # fields = ['id','restaurant','name']
        fields = ('__all__')