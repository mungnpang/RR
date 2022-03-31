from bookmark.models import Bookmark
from user.models import UserModel
from repositories.models import Repositories
from django.db.utils import IntegrityError


def CREATE_BOOKMARK(user_id: int, repo_id: int) -> str:
    if not UserModel.objects.filter(id=user_id).exists():
        return True, "User is None"
    if not Repositories.objects.filter(id=repo_id).exists():
        return True, "Repository is None"
    Bookmark.objects.create(
            user_id = user_id,
            repo_id = repo_id
            )
    return False, "Create Success"