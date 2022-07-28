from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import user
from .forms import studentreg


#This will add data.
def addshow(request):
    if request.method == 'POST':
        fm = studentreg(request.POST)
        if fm.is_valid():
            fm.save()
        fm= studentreg()
    else:
        fm = studentreg()
    stud = user.objects.all()
    return render(request,'student/addshow.html',{'form':fm ,'stu':stud})

#This will update data.
def update_data(request , id):
    if request.method=="POST":
        pi =user.objects.get(pk=id)
        fm = studentreg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm= studentreg(instance=pi)

    return render(request,'student/update.html', {'form':fm})

#This will delete data.
def delete_data(request,id):
    if request.method =="POST":
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

