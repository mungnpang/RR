from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class UserModel(AbstractUser):
    class Meta:
        db_table = "users"
    email = models.CharField(max_length=254, unique= True, null=False)
    username = models.CharField(max_length=150, unique=True, null=True)
    visit_count = models.IntegerField(default=0)
    last_visit = models.DateTimeField(default=now, null= True)

