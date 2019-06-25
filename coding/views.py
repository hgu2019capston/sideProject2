from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django import forms

from .forms import CodingForm
from .models import Coding
from .makeFile import file
from .runFile import runfile

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
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)
