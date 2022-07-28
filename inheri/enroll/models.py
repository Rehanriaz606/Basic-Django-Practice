from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    school_id = models.CharField(max_length=40)
    age =  models.IntegerField()