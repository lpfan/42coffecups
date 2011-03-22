from django import template
from django.core.urlresolvers import reverse

register = template.Library()

def create_link(obj):
    link = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.module_name), args=[obj.id])
    #link = u'<a href="/admin/%s/%s/%i" title="edit">edit %s</a>'%(obj._meta.app_label, obj._meta.module_name, obj.id, obj.__unicode__())
    return unicode(link)
    
class AdminEditNode(template.Node):
    def __init__(self, object):
        self.object = template.Variable(object)
        
    def render(self, context):
        return create_link(self.object.resolve(context))

def admin_edit(parser, token):
    tagname, object = token.split_contents()
    return AdminEditNode(object)

register.tag('admin_edit', admin_edit)