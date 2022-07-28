"""inheri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path
from enroll import views

from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MyView.as_view(name='Tariq'),name='home'),
    path('employee/',views.Employee_view.as_view(),name='employee'),
    path('student/',views.student_view),
    path('teacher/',views.Teacher_view.as_view()),
    path('home/',views.HomeTemplateView.as_view(extra_context={'class':'FSC','age':18},template_name='myhome.html'),name='myhome'),
    path('rehan/',TemplateView.as_view(template_name='myhome.html'),name='Hello')
    

]
