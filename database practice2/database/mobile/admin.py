from django.contrib import admin
from .models import omobile
# Register your models here.
class user(admin.ModelAdmin):
    list_display= ['id','o_id','o_model','o_price']
admin.site.register(omobile,user)