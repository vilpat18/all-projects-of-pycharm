from .models import OdiBattingRecord
from .serialisers import OdiBattingRecordSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class OdiRecordModelViewSet(viewsets.ModelViewSet):
    queryset = OdiBattingRecord.objects.all()
    serializer_class = OdiBattingRecordSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]