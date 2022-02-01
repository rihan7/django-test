from store.models import Product, Variation
from django.contrib import admin

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    readonly_fields = ('created_at', 'modified_at', )


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'variation_category', 'variation_value', 'is_active',)
    list_editable = ('is_active',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
