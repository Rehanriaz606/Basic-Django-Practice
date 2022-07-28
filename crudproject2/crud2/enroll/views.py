from django.shortcuts import render, HttpResponseRedirect
from sympy import Id
from .models import user
from .froms import studentregistration

# This will Addshow.
def addshowview(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = studentregistration()
    else:
        fm = studentregistration()
    stud = user.objects.all()
    return render(request,'student/addshow.html',{'form':fm,'stu':stud})

#this function will update and edit.
def updateview(request, id):
    if request.method == 'POST':
        up = user.objects.get(pk=id)
        fm = studentregistration(request.POST, instance=up)
        if fm.is_valid():
            fm.save()
    else:
        up = user.objects.get(pk=id)
        fm = studentregistration(instance=up)
    return render (request,"student/update.html",{'form':fm})

#This function will delete.
def deleteview(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
