from django.db import models
from django.db.models.fields import AutoField
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 20)
    weight = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        app_label='Products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'Product'
    
    def __str__(self):
        return self.name