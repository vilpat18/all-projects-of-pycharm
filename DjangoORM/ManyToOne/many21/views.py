from django.shortcuts import render

# Create your views here.
from .models import Reporter,Article
from .serialisers import ReporterSerializer,ArticleSerializer
from rest_framework import viewsets

class ReporterAPIView(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class ArticleAPIView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer