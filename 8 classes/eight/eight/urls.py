"""eight URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from no1 import views as no1
from no2 import views as no2
from no3 import views as no3
from no4 import views as no4
from no5 import views as no5

urlpatterns = [
    path('admin/', admin.site.urls),
    path('no1/',include ('no1.urls')),
    path('no2/',include('no2.urls')),
    path('no3/',include('no3.urls')),
    path('no4/',include('no4.urls')),
    path('no5/',include('no5.urls')),
    ]
