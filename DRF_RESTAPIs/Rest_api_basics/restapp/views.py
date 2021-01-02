from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from django.db.models import Q


class BlogPostCreateList(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
        # qs = BlogPost.objects.all()
        # query = self.request.get('q')
        # if query is not None:
        #     qs = qs.filter(Q(title__icontains=query)|
        #                    Q(content__icontains=query)).distinct()
        #     return qs


class BlogPostRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()


