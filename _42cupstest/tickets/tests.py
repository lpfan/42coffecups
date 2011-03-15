from django.test import TestCase, Client

from models import MyInfo, RequestStore
from forms import EditMyInfoForm

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
         
class EditMyInfoTest(TestCase):
    def setUp(self):
        client = Client()
    
    def testEditPage(self):
        self.client.login(username="testuser", password="12345")
        resp = self.client.get('/editmyinfo/')
        self.assertEqual(resp.status_code, 302)
        data = {"surname" :"shchetinin",
                "name"    : "misha",
                "bday"    : "1989-11-26",
                "contacts": "skype_id: pro-finder",
                "short_story": "All because of you I belive in angels. Not a kind with wings. No, not I kind with halos."
        }
        form = EditMyInfoForm(data)
        self.assertTrue(form.is_valid())
        data = {"surname" : None,
                "bday"    : "1989-26-11"}
        form = EditMyInfoForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue('surname' in form.errors)
        self.assertTrue('name' in form.errors)
        self.assertTrue('bday' in form.errors)
        self.assertTrue('contacts' in form.errors)
        self.assertTrue('short_story' in form.errors)
        
    def testReverseForm(self):
        form = EditMyInfoForm()
        field_list = [key for key in form.fields]
        self.assertEqual(field_list[0], 'short_story')
        self.assertEqual(field_list[1], 'bday')
        
        
