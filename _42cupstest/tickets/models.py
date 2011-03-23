from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

from datetime import datetime

class MyInfo(models.Model):
  surname = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  bday = models.DateField()
  contacts = models.TextField()
  short_story = models.TextField()
  
  def __unicode__(self):
    return "name: %s, surname: %s" % (self.name, self.surname)

class RequestStore(models.Model):
  host = models.CharField(max_length=255)
  path = models.CharField(max_length=255)
  method = models.CharField(max_length=100)
  user = models.ForeignKey(User, blank=True, null=True)
  date = models.DateTimeField(default=datetime.now() )
  
class ModelStatus(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    
def model_status_saver(sender, **kwargs):
    #file = open('/home/misha/eclipse/_42cupstest/model_log','w+')
    #file.write(sender._meta.object_name)
    #file.close()
    if sender._meta.object_name == 'ModelStatus': 
        return
    model_status = ModelStatus()
    model_status.model = sender._meta.object_name
    model_status.action = 'create or edit'
    model_status.save()

post_save.connect(model_status_saver)
post_delete.connect(model_status_saver)   