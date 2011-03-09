from django.views.generic.simple import direct_to_template

from models import MyInfo

def contact(request, template_name="contact.html"):
    info = MyInfo.objects.get(pk=1)
    return direct_to_template(request, template_name, {"title":'contact', "info":info})