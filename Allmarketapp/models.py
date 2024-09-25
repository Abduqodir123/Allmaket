from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255) #Product ismi
    description = models.TextField(blank=True) #Product comentariyasi
    price = models.DecimalField(max_digits=10, decimal_places=2) #Product narxi
    image = models.ImageField(upload_to='post_image/', blank=True, null=True) #Product rasmi
    view_count = models.IntegerField(default=0) #Product korilgan soni
    like_count = models.IntegerField(default=0) #Product layk soni

    def __str__(self):
        return self.name

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Foydalanuvchi bilan aloqa
    products = models.ManyToManyField(Product, related_name='orders') #Buyurtmani zakaz qilinvoti
    created_at = models.DateTimeField(auto_now_add=True) #zakaz qilingan vaqt
    is_ordered = models.BooleanField(default=False) #aformleniya

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart') #Foydalanuvchi bilan aloqa
    product = models.ManyToManyField(Product, related_name='carts') #karzinadigi productla
    created_at = models.DateTimeField(auto_now_add=True) #Karzina yaratilgan vaqt

    def __str__(self):
        return f"Cart of {self.user.username}"

