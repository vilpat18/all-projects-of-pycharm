from .models import OdiBattingRecord
from .serialisers import OdiBattingRecordSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class OdiRecordModelViewSet(viewsets.ModelViewSet):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]