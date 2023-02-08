from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def django_forms(request):
    formobject=studentform()
    d={'forms':formobject}

    if request.method=="POST":
        FD=studentform(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'django_forms.html',d)