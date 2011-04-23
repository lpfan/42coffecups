from django.db import models

class MyInfo(models.Model):
  
  surname = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  bday = models.DateField()
  email = models.EmailField()
  jabber_id = models.CharField(max_length=100)
  skype_id = models.CharField(max_length=100)
  other_contacts = models.TextField()
  bio = models.TextField()
  
  def __unicode__(self):
    return "name: %s, surname: %s" % (self.name, self.surname)
