from django.contrib import admin
from .models import student
# Register your models here.

class user(admin.ModelAdmin):
    list_display = ['rollno','name','email']

admin.site.register(student,user)