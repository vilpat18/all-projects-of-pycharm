from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serialisers import OdiBattingRecordSerializer
from .models import OdiBattingRecord
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter,OrderingFilter

class ListApiView(generics.ListAPIView):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ('name','country','runs')


