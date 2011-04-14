from django.views.generic.simple import direct_to_template

from models import MyInfo

def index(request, template_name="index.html"):
    return direct_to_template(request, template_name, {'title':'start page'})

def contacts(request, template_name="contact.html"):
    info = MyInfo.objects.get()
    return direct_to_template(request, template_name, {"title":'contact', "info":info})