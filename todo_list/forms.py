from django import forms
from .models import List


class FormList(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
