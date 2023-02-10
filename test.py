# pages/tests.py
from django.test import SimpleTestCase
#from django.urls import urlpatterns  


class HomepageTests(SimpleTestCase):
    def test_base_url_not_found(self):
        response = self.client.get("http://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 404)
    def test_wpscan(self):  
        response = self.client.get(("http://127.0.0.1:8000/cyan_api?scanner=wpscan&url=sharksec.net"))
        self.assertEqual(response.status_code, 200)
    #def test_namp(self):  
    #    response = self.client.get(("http://127.0.0.1:8000/cyan_api?scanner=nmap&url=sharksec.net"))
    #    self.assertEqual(response.status_code, 200)
    #def test_nikto(self):  
    #    response = self.client.get(("http://127.0.0.1:8000/cyan_api?scanner=nikto&url=sharksec.net"))
    #    self.assertEqual(response.status_code, 200)
    def test_verify_db_results(self):  
        response = self.client.get(("http://127.0.0.1:8000/cyan_api/results/by_url?url=sharksec.net"))
        self.assertEqual(response.status_code, 200)

