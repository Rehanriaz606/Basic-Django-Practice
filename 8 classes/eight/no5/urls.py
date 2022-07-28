from django.urls import path 
from . import views
urlpatterns = [

 path('full/',views.full),
 path('mid/',views.mid),
 path('half/',views.half),

]


