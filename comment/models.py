from django.db import models
from user.models import UserModel
from repositories.models import repositories


class Comment(models.Model):
    repo = models.ForeignKey(repositories, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "comments"