from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from models import MyInfo, RequestStore
from forms import EditMyInfoForm

def index(request, template_name="index.html"):
    return direct_to_template(request, template_name, {"title":'start page'})

def contact(request, template_name="contact.html"):
    info = MyInfo.objects.get()
    return direct_to_template(request, template_name, {"title":'contact', "info":info})

def request_store(request, template_name="show_requests.html"):
    requests = []
    requests.extend(RequestStore.objects.filter(priority=1))
    requests.extend(RequestStore.objects.exclude(priority=1))
    return direct_to_template(request, template_name, {'requests':requests, 'title':"stored requests"})
  
def show_settings(request, template_name="show_settings.html"):
    return direct_to_template(request, template_name, {'title':"show project settings"})

@login_required
def edit_my_info(request, template_name="editpage.html"):
    info = MyInfo.objects.get()
    if request.method == 'POST':
        form = EditMyInfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact/')
    form = EditMyInfoForm(instance=info)    
    return direct_to_template(request, template_name, {"form":form, "title":"Edit page"})

def contacts(request, template_name="contact.html"):
    info = MyInfo.objects.get()
    return direct_to_template(request, template_name, {"title":'contact', "info":info})

