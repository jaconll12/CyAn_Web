from turtle import pd
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from .test_setup import TestSetUpCyAn, TestSetUpResults
import json

from CyAn.views import cyan
class TestViews(TestSetUpCyAn):
    def test_post(self):
        print (self.register_url)
        res = self.client.post(
            self.register_url, self.user_data, format="json")
        print (self.register_url, res.items)
        self.assertEqual(res.status_code, 200)

    def test_get(self):
        print (self.register_url)
        resp = self.client.get(
            self.register_url+"?scanner=nmap&url=www.google.com")
        print (self.register_url, resp.items)
        self.assertEqual(resp.status_code, 200)
    def test_get_error(self):
        print (self.register_url)
        resp = self.client.get(
            self.register_url+"scanner=test&url=www.google.com")
        print (self.register_url, resp.items)
        self.assertEqual(resp.status_code, 404)


class TestViewsResults(TestSetUpResults):
    def test_post(self):
        print (self.register_url)
        res = self.client.get(
            self.register_url+"?url=www.google.com")
        self.assertEqual(res.status_code, 200)
        