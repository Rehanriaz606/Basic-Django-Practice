from django.db import models
from matplotlib import widgets
from requests import request

# Create your models here.
class m_data(models.Model):
    h_id = models.IntegerField()
    h_name = models.CharField(max_length=100)
    h_email = models.EmailField()