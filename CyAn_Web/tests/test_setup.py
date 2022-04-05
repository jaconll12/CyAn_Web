from unittest import result
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from CyAn.views import cyan, results





class TestSetUpCyAn(APITestCase):
    def setUp(self):
        self.register_url = reverse(cyan)
        self.user_data={
            'scanner': 'nmap',
            'url': 'www.google.com'
        }    
        return super().setUp()
class TestSetUpResults(APITestCase):
    def setUp(self):
        self.register_url = reverse(results)
        self.user_data={
            'url': 'www.google.com'
        }    
        return super().setUp()