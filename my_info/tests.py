from django.test import TestCase

from models import MyInfo

class ModelTest(TestCase):    
  fixtures = ['my_info.json']
  info = Info.objects.get(pk=1)
  def testMyInfo(self):
    '''
      test data loaded from fixtures
    '''
    for arg in info:
      self.assertTrue(arg)

class ViewTest(TestCase):
  '''
    Test main page view
  '''
  def testMainPage(self):
    main_page = self.client.get('')
    self.assertEqual(main_page.status_code, 200)
    self.assertTrue(main_page.context['surname'])
    self.assertTrue(main_page.context['name'])
    self.assertTrue(main_page.context['bday'])
    self.assertTrue(main_page.context['contacts'])
    self.assertTrue(main_page.context['short_story'])


