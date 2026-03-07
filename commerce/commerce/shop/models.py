from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50 ,default="")
    category=models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=100 ,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/image")
