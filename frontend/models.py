from django.db import models

# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to = 'frontend/images/') # blank is the property we can add anything to

    def __str__(self):
        return self.productname




