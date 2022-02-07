from urllib import request
from django.shortcuts import render

# Create your views here.

def HomePageView(render):
    return render(request, 'home.html')