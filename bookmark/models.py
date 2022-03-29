from django.db import models
from repositories.models import Repositories
from user.models import UserModel

# Create your models here.

class Bookmark(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    repo = models.ForeignKey(Repositories, on_delete=models.CASCADE)
    

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "repo"], name="unique_user_repo")]
        db_table = "bookmark"