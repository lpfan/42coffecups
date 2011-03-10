from django.conf.urls.defaults import *

urlpatterns = patterns('tickets.views',
    url('contact/$', 'contact'),
    url('request_store/$', 'request_store'),
    )