from django.contrib import admin
from .models import m_pencil
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ['id','p_name','p_price']

admin.site.register(m_pencil,user)


