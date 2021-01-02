from django.shortcuts import render

# Create your views here.

from Cncapp.models import OdiBattingRecord
from Cncapp.serialisers import OdiBattingRecordSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,\
     DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,RetrieveDestroyAPIView

class OdiListApiView(ListAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

class OdiCreateAPIView(CreateAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

class OdiUpdateAPIView(UpdateAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer


class OdiRetrieveAPIView(RetrieveAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

class OdiDestroyAPIView(DestroyAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer


class RecordsListCreateAPIView(ListCreateAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer


class RecordRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

class RecordRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer


class RecordRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

