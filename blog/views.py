from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render

def homepage(request):
    return render(request, "blog/index.html")