from django.forms import ModelForm
from django import forms
from codemirror import CodeMirrorTextarea
from .models import Coding

class CodingForm(forms.Form):

    codemirror_widget = CodeMirrorTextarea(
            mode = 'python',
            theme = 'cobalt',
            config = {
                    'fixedGutter': True
                    },
    )

    content = forms.CharField(widget=codemirror_widget)

    def save(self, commit=True):
        coding = Coding(**self.cleaned_data)
        if commit:
            coding.save()
        return coding
