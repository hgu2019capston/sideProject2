from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

from .forms import CodingForm
from .models import Coding
from .makeFile import file
from .runFile import runfile
import json

from django.http import JsonResponse

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
		return JsonResponse({"result":result}, status=200)
	return JsonResponse({"result":False}, status=400)
