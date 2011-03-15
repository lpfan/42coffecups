from django import forms
from models import MyInfo

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
               'all': ('css/ui-lightness/jquery-ui-1.8.10.custom.css',),
        }
        
        js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4/jquery.min.js", 
              "http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/jquery-ui.min.js",
              )
    
class EditMyInfoForm(forms.ModelForm):
    class Meta:
        model = MyInfo
        info = MyInfo.objects.all()
        field_list=list()
        for arg in info.values()[:1]:
            for key in arg:
                field_list.append(key)
        field_list.reverse()
        fields = tuple(field_list)
        widgets = {
                   'bday':CalendarWidget,
                   }
        