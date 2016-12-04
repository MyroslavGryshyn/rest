from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class Key(models.Model):
    class Meta:
        db_table = 'token'

    user = models.OneToOneField(CustomUser)
    key = models.CharField(max_length=40, unique=True)


class Post(models.Model):
    class Meta:
        db_table = 'post'

    user = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    date = models.DateTimeField(blank=True, auto_now_add=True)
