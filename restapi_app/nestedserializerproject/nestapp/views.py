from django.shortcuts import render

# Create your views here.

from nestapp.models import Author , Book
from nestapp.serializers import AuthorSerializer , BookSerializer
from rest_framework import generics

class AuthorListview(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetriveUpdateDestroyview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListview(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetriveUpdateDestroyview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
