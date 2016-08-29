from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from forms import confessionForm, ConfessionForm
from .models import Confession


# Create your views here.

def index(request):
    """    #print request.POST
        form = confessionForm(request.POST or None)
        if form.is_valid():
            c= form.cleaned_data['confession']
            new_join, created = Confession.objects.get_or_create(confession=c)
            print new_join, created
        return render(request,"confession/index.html", {"form": form})
    """
    form = ConfessionForm(request.POST or None)
    if form.is_valid():
        new_confessions = form.save(commit=False)
        new_confessions.save()
    return render(request,"confession/index.html", {"form": form})

def confession(request):
    print request.POST
    form = confessionForm
    return render(request,"confession/index.html", {"form": form})

def confess(request):
    if request.method == "POST" : pass
    return HttpResponse("ose")
