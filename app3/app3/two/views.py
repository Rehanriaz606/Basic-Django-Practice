from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pin(request):
    return render(request,'static.html')