from django.shortcuts import render

# Create your views here.
from .models import Article,Publication
from .serialisers import ArticleSerializer,PublicationSerializer
from rest_framework import viewsets


class ArticleAPIView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PublisAPIView(viewsets.ModelViewSet):
    queryset = Publication
    serializer_class = PublicationSerializer