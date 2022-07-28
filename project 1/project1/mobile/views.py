from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sympy import product

def samsung(request):
    samsung= {'name':'samsung','price':'320$','RAM':'4GB'}
    return render(request,'mobile.html',samsung)

def huawei(request):
    huawei= {'name':'huawei','price':'300$','RAM':'6GB'}
    return render (request,'mobile.html',huawei)

def oppo(request):
    oppo= {'name':'oppo','price':'720$','RAM':'8GB'}
    return render(request,'mobile.html',oppo)