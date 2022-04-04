from django.db import models
from user.models import UserModel
from bookmark.models import Bookmark
from repositories.models import Repositories
from comment.models import Comment
from django_mysql.models import ListCharField


# Create your models here.
class Mypage(models.Model):
    class Meta:
        db_table = "mypage"
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    recently_visit = ListCharField(
        base_field = models.IntegerField(),
        max_length = (6*40),
        default=[]
    )
    recently_recommand = ListCharField(
        base_field = models.IntegerField(),
        max_length = (6*40),
        default=[]
    )

    
