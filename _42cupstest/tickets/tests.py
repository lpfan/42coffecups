from django.test import TestCase
from django.test import Client

from models import MyInfo, RequestStore

class ModelTest(TestCase):    
  fixtures = ['initial_data.json']
  info = MyInfo.objects.get(pk=1)
  def testMyInfo(self):
    '''
      test data loaded from fixtures
    '''
    self.assertTrue(self.info.surname)
    self.assertTrue(self.info.name)
    self.assertTrue(self.info.bday)
    self.assertTrue(self.info.contacts)
    self.assertTrue(self.info.short_story)

class RequestStoreTest(TestCase):
  def testMiddleware(self):
    client = Client()
    resp = client.get('/request_store/')
    self.assertEqual(resp.status_code, 200)
    req_store = RequestStore.objects.get(path = resp.request["PATH_INFO"])
    self.assertTrue(req_store)
    
class ContextProcessorTest(TestCase):
    def testC_Processor(self):
         client = Client()
         resp = client.get('/index/')
         self.assertEqual(resp.status_code, 200)
         self.assertTrue(resp.context['settings'], "Your context-processor didn't add settings to template-context")
