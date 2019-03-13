from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from codemirror import CodeMirrorTextarea
from django import forms

from .forms import CodingForm
from .models import Coding

def get_code(request):
    if request.method == 'POST':
        form = CodingForm(request.POST)
        if form.is_valid():
                 coding = form.save()
                 coding.generate()
        return HttpResponse(coding)
   
    else :
        form = CodingForm()

    return render(request, 'coding/name.html',{'form':form})

