from django.contrib import admin
from .models import m_computer
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ['c_id','c_model','c_price']
admin.site.register(m_computer,user)