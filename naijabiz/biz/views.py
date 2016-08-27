from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
import datetime, time
from .models import Biz
# Create your views here.


def index(request):
    bizs = Biz.objects.order_by('name')
    return render_to_response("biz/index.html", {"bizs": bizs })

def home(request):
    return render_to_response("biz/home.html", {'hello': "Welcome to africa biz"},
                              )
