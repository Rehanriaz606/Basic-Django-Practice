from django.contrib import admin
from .models import movies
from .models import Genre

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display= ('id','name')

class MoviesAdmin(admin.ModelAdmin):
    exclude= ("date_created",)
    list_display =('title','release_year','daily_rate','Genre') 
admin.site.register(movies,MoviesAdmin)
admin.site.register(Genre,GenreAdmin)

