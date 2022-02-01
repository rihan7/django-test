from categories.models import Categories
from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    slug = models.SlugField(max_length=100, unique=True)
    product_image = models.ImageField(upload_to='photos/product')
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_view', args=[self.categories.slug, self.slug])


class Variation_manager(models.Manager):
    def get_by_color(self):
        return super(Variation_manager, self).get_queryset().filter(variation_category="color")

    def get_by_size(self):
        return super(Variation_manager, self).get_queryset().filter(variation_category="size")


variation_choice = (('size', 'Size'), ('color', 'Color'))


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    variation_category = models.CharField(
        max_length=100, choices=variation_choice)
    variation_value = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = Variation_manager()

    def __str__(self):
        return self.product.product_name
