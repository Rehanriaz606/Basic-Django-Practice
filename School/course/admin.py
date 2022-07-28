from django.contrib import admin
from .models import User
from .models import AdminUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']
admin.site.register(User,UserAdmin)

class UserAdminAdmin(admin.ModelAdmin):
    list_display = ['name','email','password']
admin.site.register(AdminUser,UserAdmin)