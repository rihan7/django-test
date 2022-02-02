from cart.models import Cart, CartItem
from django.contrib import admin

# Register your models here.


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)
