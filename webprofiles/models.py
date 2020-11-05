from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class EmployeeProfiles(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    first_name = models.CharField(max_length=10, )
    last_name = models.CharField(max_length=10, )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.email,  self.first_name+self.last_name
