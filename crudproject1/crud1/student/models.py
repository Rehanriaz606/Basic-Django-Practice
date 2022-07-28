import email
from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=90)
    password = models.CharField(max_length=100)