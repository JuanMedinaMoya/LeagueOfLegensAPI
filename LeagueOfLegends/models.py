
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User as Usuario
from django.contrib.auth.models import PermissionsMixin
import uuid

class User(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE,blank=False, unique=True, default=None)
    lolusername = models.CharField(default="",max_length=255)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 
    def __str__(self):
        return self.user.username

class Friend(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    friend = models.CharField(max_length=255, blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 


# Create your models here.
