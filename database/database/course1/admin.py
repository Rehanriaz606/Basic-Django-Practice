from django.contrib import admin

#from database.course1.forms import course
from django.contrib import admin
from . models import student
# Register your models here.
class user (admin.ModelAdmin):
    list_display = ['id','stuid','stuname','stuemail','stupassword']
admin.site.register(student,user)