from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .manager import AppUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that supports using email instead of username
    """

    email = models.EmailField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = AppUserManager()

    USERNAME_FIELD = "username"

    class Meta:
        managed = True
        indexes = [models.Index(fields=["username"])]
