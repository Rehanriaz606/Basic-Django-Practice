from django.db import models

# Create your models here.
class m_pencil(models.Model):
    p_id = models.IntegerField()
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()