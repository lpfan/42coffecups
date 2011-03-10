from django.db import models
from django.contrib.auth.models import User

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