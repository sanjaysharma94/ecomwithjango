from django.db import models

# Create your models here.

class Product(models.Model):
    product_Id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300, default="")
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(upload_to="" , default="")

    def __str__(self):
        return self.product_name
