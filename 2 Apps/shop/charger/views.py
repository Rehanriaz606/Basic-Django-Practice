from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def hp(request):
    hp = {'name':'hp','price':'400$','weight':"250"}
    return render(request,'laptops.html',hp)

def lenovo(request):
    lenovo = {'name':'lenovo','price':'340$','weight':'230'}
    return render(request,'laptops.html',lenovo)

def dell(request):
    dell = {'name':'dell','price':'340$','weight':'230'}
    return render(request,'laptops.html',dell)

def macbook(request):
    macbook = {'name':'macbook','price':'340$','weight':'230'}
    return render(request,'laptops.html',macbook)

def toshiba(request):
    toshiba = {'name':'toshiba','price':'340$','weight':'230'}
    return render(request,'laptops.html',toshiba)