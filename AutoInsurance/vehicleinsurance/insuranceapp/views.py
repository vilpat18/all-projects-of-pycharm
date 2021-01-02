from django.shortcuts import render

# Create your views here.
from .models import Policy,PolicyEditLog,Bill,Payment,Driver,Vehicle,Coverage
from .serialisers import PolicySerializer,PolicyEditLogSerializer,BillSerializer,\
                         PaymentSerializer,DriverSerializer,VehicleSerializer,CoverageSerializer

from rest_framework import viewsets


class PolicyAPIView(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class PolicyEditLogAPIView(viewsets.ModelViewSet):
    queryset = PolicyEditLog.objects.all()
    serializer_class = PolicyEditLogSerializer


class BillAPIView(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class PaymentAPIView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class DriverAPIView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleAPIView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class CoverageAPIView(viewsets.ModelViewSet):
    queryset = Coverage.objects.all()
    serializer_class = CoverageSerializer


