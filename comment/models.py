from django.db import models
from pydantic import validator

from repositories.models import Repositories
from user.models import UserModel


class Comment(models.Model):
    repo = models.ForeignKey(Repositories, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    reply = models.IntegerField(default=0)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
