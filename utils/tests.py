from django.test import TestCase
from django.test import Client
from models import RequestStore

class RequestStoreTest(TestCase):
  def testMiddleware(self):
    client = Client()
    resp = client.get('/request_store/')
    self.assertEqual(resp.status_code, 200)
    req_store = RequestStore.objects.get(path = resp.request["PATH_INFO"])
    self.assertTrue(req_store) 
    

