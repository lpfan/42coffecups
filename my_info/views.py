from django.generic.simple import direct_to_template
from models import MyInfo

def index(request):
  info = MyInfo.objects.get(pk=1)
  return direct_to_template(request, "index.html" , {"surname"     : info.surname,
						     "name"        : info.name,
						     "bday"        : info.bday,
						     "contacts"    : info.contacts,
						     "short_story" : info.short_story
						    })