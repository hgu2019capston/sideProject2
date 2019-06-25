from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

from .forms import CodingForm
from .models import Coding
from .makeFile import file
from .runFile import runfile
import json

from django.http import JsonResponse

def get_code(request):
    if request.method == 'POST':
        form = CodingForm(request.POST)
        if form.is_valid():
                 Coding = form.save()
                 Coding.generate()
                 file(Coding.languages)
                 result=runfile(Coding.languages)
        return HttpResponse(result)
   
    else :
        form = CodingForm()

    return render(request, 'coding/name.html',{'form':form})


#FBV
def codePage(request):
	form = CodingForm()
	return render(request, "coding/name.html", {"form": form})

def postCode(request):
	if request.method == "POST" and request.is_ajax():
		form = CodingForm(request.POST)
		Coding = form.save()
		Coding.generate()
		file(Coding.languages)
		result = runfile(Coding.languages)
		result = result.decode('utf-8')
		return JsonResponse({"success":result}, status=200)
	return JsonResponse({"success":False}, status=400)
