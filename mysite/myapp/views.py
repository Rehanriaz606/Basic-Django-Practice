from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('home page')
def main(request):
    return render(request,'main.html')
def register(request):
    return render(request,'register.html')