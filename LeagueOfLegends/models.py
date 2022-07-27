from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.username

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    friend = models.CharField(max_length=255, blank=True)


# Create your models here.
