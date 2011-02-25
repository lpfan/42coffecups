from models import RequestStore
from django.views.generic.simple import direct_to_template

def request_store(request, template="show_requests.html"):
  requests = RequestStore.objects.all()
  return direct_to_template(request, template, {'requests':requests}
  
