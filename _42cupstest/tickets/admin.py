from django.contrib import admin
from models import MyInfo

class MyInfoEditAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyInfo, MyInfoEditAdmin)