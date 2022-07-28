from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'hello':'This is Home Page'})

def about(request):
    return render(request,'index.html',{'hello':'This is About Us Page'})


def contact(request):
    return render(request,'index.html',{'hello':'This is Contact Us Page'})

def career(request,id):
    return render(request,'career.html',{'hello':'This is Career Opportunity Page','id':id})