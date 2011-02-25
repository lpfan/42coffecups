from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class RequestStore(models.Model):
  host = models.CharField(max_length=255)
  path = models.CharField(max_length=255)
  method = models.CharField(max_length=100)
  user = models.ForeignKey(User,blanck=True, None=True)
  date = models.DateTimeField(default=datetime.now() )
