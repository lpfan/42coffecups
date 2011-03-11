from django.forms import ModelForm
from models import MyInfo

class EditMyInfoForm(ModelForm):
    class Meta:
        model = MyInfo