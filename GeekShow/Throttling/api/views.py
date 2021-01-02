from django.shortcuts import render

# Create your views here.
from .models import OdiBattingRecord,BowlingRecord
from .serialisers import OdiBattingRecordSerializer,BowlingRecordSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework import viewsets

class OdiRecordAPI(viewsets.ModelViewSet):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]

class BowlingRecordAPI(viewsets.ModelViewSet):
    queryset = BowlingRecord.objects.all()
    serializer_class = BowlingRecordSerializer
