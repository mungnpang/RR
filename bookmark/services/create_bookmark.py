from django.db.utils import IntegrityError

from bookmark.models import Bookmark
from repositories.models import Repositories
from user.models import UserModel


def create_bookmark(user_id: int, repo_id: int) -> str:
    if not UserModel.objects.filter(id=user_id).exists():
        return False
    if not Repositories.objects.filter(id=repo_id).exists():
        return False
    Bookmark.objects.create(user_id=user_id, repo_id=repo_id)
    return True
