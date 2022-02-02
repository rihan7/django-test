from django.db import models
from store.models import Product, Variation

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=256)
    data_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_variations = models.ManyToManyField(Variation, blank=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name

    def subtotal(self):
        return self.product.price * self.quantity
