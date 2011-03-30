from django.contrib import admin
from models import MyInfo, RequestStore

class MyInfoEditAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyInfo, MyInfoEditAdmin)

class RequestStoreAdmin(admin.ModelAdmin):
    list_display = ['host', 'path', 'user', 'date', 'priority']
    list_filter = ['priority']

admin.site.register(RequestStore, RequestStoreAdmin)