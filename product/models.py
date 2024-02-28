from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "used"), (1, "new"), (2, "handmade"))

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    #image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    seller_contact = models.CharField(max_length=200)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=0)