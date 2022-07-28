from django.db import models

# Create your models here.
class student(models.Model):
    stuid =  models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField(max_length=100)
    stupassword = models.CharField(max_length=100)