from django.db import models

class MyInfo(models.Model):
  surname = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  bday = models.DateField()
  contacts = models.TextField()
  short_story = models.TextField()
  
  def __unicode__(self):
    return "name: %s, surname: %s" % (self.name, self.surname)
