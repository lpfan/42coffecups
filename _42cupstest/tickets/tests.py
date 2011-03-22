from django.test import TestCase, Client
from django.template import Template, Context
from django.db.models import get_app, get_models
from django.core.management import call_command

from models import MyInfo, RequestStore
from forms import EditMyInfoForm
from templatetags.tags import create_link

import sys, StringIO

class ModelTest(TestCase):    
  fixtures = ['initial_data.json']
  info = MyInfo.objects.get()
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
        
class TemplateTagTest(TestCase):
    def testEditLinkTag(self):
        client = Client()
        client.login(username="admin", password="12345")
        edit_obj = MyInfo.objects.get()
        admin_edit_link = create_link(edit_obj)
        t = Template("{% load tags %} {% admin_edit edit_obj %}")
        result = t.render(Context({'edit_obj' : edit_obj}))
        self.assertEqual(admin_edit_link, result)
        
class CommandTest(TestCase):
    def testCommand(self):
        output = StringIO()
        sys.stdout = output
        call_command('showmodels')
        sys.stdout = sys.__stdout__
        for model in get_models():
            self.assertNotEqual(output.getvalue().find(model), 0)
            
            
        
         
        
        
