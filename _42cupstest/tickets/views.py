from django.views.generic.simple import direct_to_template

from models import MyInfo, RequestStore

def index(request, template_name="index.html"):
    return direct_to_template(request, template_name, {"title":'index'})

def contact(request, template_name="contact.html"):
    info = MyInfo.objects.get(pk=1)
    return direct_to_template(request, template_name, {"title":'contact', "info":info})

def request_store(request, template_name="show_requests.html"):
    requests = RequestStore.objects.all()
    return direct_to_template(request, template_name, {'requests':requests, 'title':"stored requests"})
  
def show_settings(request, template_name="show_settings.html"):
    return direct_to_template(request, template_name, {'title':"show project settings"})    