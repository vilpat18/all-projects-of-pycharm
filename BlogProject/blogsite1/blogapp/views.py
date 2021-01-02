from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Post,User
from .serialisers import PostSerializer,UserSerializer


class PostAPI(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    serializer_class = PostSerializer