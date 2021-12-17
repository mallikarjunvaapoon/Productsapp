from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    products = models.FileField(upload_to='product')
    brand = models.OneToOneField(Brands, on_delete=models.CASCADE)


