from pyexpat import model
from django.db import models

# Create your models here.
class m_computer(models.Model):
    c_id= models.IntegerField()
    c_model = models.CharField(max_length=100)
    c_price = models.IntegerField()