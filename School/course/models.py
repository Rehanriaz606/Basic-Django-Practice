from django.db import models
from matplotlib import widgets

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)


class AdminUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)

    