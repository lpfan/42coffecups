from django.conf.urls.defaults import *

urlpatterns = patterns('tickets.views',
    url('request_store/$', 'request_store'),
    url('show_settings/$', 'show_settings'),
    url('editmyinfo/$', 'edit_my_info'),
    url('contacts/$', 'contacts'),
    )