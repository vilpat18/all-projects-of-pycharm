from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.urls import re_path


class BlogPostAPITestCase(APITestCase):

    def testblogPost(self):
        data = {'user':'sachin','title':'engineer','content':'hgdjfgsseabcd','timestamp': '2012-10-10'}
        response = self.client.post('/api/post/list/',data)
        self.assertEquals(response.status_code,status.HTTP_201_CREATED)






