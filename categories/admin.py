from categories.models import Categories
from django.contrib import admin

# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['category_name']}


admin.site.register(Categories, CategoriesAdmin)
