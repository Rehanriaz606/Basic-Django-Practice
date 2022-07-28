from urllib.parse import urlparse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def clock(request):
    return render(request,'static.html')
