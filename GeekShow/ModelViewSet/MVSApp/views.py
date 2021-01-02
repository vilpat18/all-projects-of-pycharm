from django.shortcuts import render

# Create your views here.
from .models import OdiBattingRecord
from .serialisers import OdiBattingRecordSerializer
from rest_framework import viewsets
from django.db.models import Q


class OdiRecordModelViewSetAPI(viewsets.ModelViewSet):
    serializer_class = OdiBattingRecordSerializer
    queryset = OdiBattingRecord.objects.all()

    # def get_queryset(self):
    #     qs = OdiBattingRecord.objects.all()
    #     query = self.request.get('q')
    #     if query is not None:
    #         qs = qs.filter(Q(name__icontains=query)|
    #                        Q(runs__icontains=query))
    #         return qs


class RecordReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer

