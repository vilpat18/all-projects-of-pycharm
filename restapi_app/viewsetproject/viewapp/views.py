from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from viewapp.models import Players
from viewapp.serializers import PlayerSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from viewapp.permissions import IsReadOnly ,IsGetOrPatch,RohitPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from viewapp.authentications import CustomaAthentication
class PlayerCRUDCBV(ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer
    authentication_classes = [CustomaAthentication]
    # authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [IsReadOnly] #our own permission class which is defines in permissions.py file its not default
    # permission_classes = [IsGetOrPatch]
    # permission_classes = [IsAuthenticated]

# from rest_framework.generics import ListAPIView
# class PlayerViewList(ListAPIView):  filtering concept
#     queryset = Players.objects.all()
#     serializer_class = PlayerSerializer
#     def get_queryset(self):
#         qs = Players.objects.all()
#         name = self.request.GET.get('pname')
#         if name is not None:
#             qs = qs.filter(pname_icontains=name)
#         return qs
