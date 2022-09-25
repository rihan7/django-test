from accounts.manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# Create your models here.


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=256)
    username = models.CharField(unique=True, max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    data_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural = 'Users'
