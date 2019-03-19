
from django.forms import ModelForm
from django import forms
#from codemirror import CodeMirrorTextarea
from .models import Coding

class CodingForm(ModelForm):

    class Meta:
        model = Coding
        fields = ['languages','content']

    def save(self, commit=True):
        coding = Coding(**self.cleaned_data)
        if commit:
            coding.save()
        return coding
