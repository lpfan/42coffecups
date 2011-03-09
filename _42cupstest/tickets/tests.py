from django.test import TestCase

from models import MyInfo

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
