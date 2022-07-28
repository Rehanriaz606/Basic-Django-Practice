from django.contrib import admin
from details.models import m_data
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ['h_id','h_name','h_email']

admin.site.register(m_data,user)
