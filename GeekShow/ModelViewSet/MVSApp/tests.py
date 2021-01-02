from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status


class OdiBattingRecordTest(APITestCase):

    def testOdiRecord(self):
        data = {'name': 'ajay', 'country': 'india', 'runs': 9999, 'fifties': 25, 'centuries': 14, 'double_centuries': 2}
        response = self.client.post('/OdiRecord/', data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)




