from django.db import models

# Create your models here.
class omobile (models.Model):
    o_id = models.IntegerField()
    o_model = models.CharField(max_length=100)
    o_price = models.IntegerField()
