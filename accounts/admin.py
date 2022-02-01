from accounts.models import CustomUserModel
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'is_admin')
    list_filter = ('email',)

    fieldsets = (
        ('Personal', {'fields': ('first_name',
         'last_name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin')}),
        ('Group', {'fields': ('user_permissions', 'groups')})
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUserModel, CustomUserAdmin)
