
from django.forms import ModelForm
from django import forms
#from codemirror import CodeMirrorTextarea
from .models import Coding

class CodingForm(ModelForm):

    class Meta:
        model = Coding
        fields = ['languages','content']
   
    def __init__(self, *args, **kwargs):
        super(CodingForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
 
