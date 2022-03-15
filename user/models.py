from operator import mod
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    class Meta:
        db_table = "users"
    email = models.CharField(max_length=254, unique= True, null=False)
    username = models.CharField(max_length=150, unique=False, null=True)
    nickname = models.CharField(max_length=15, unique=True)
    
