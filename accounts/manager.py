from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):

        if not email:
            raise ValueError('Email is required')

        if not username:
            raise ValueError('Username is required')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        user = self.create_user(email, username, password, **extra_fields)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
