from django.contrib import admin
from .models import Student
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ['name','school_id','age']

admin.site.register(Student,user)
