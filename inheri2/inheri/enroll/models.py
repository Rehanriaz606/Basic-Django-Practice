from django.db import models
from sqlalchemy import true

# Create your models here.
class student(models.Model):
    rollno = models.IntegerField(max_length=1000, primary_key=true)
    name = models.CharField(max_length=100)
    email = models.EmailField()
