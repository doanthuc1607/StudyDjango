# file này de xu ly data cho form
from django import forms
from django.forms import ModelForm

from .models import *

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'