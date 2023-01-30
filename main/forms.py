from django import forms
from .models import *


class InputIdForm(forms.Form):
    id = forms.CharField(max_length=255)

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = '__all__'