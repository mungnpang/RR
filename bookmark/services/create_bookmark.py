from bookmark.models import Bookmark
from user.models import UserModel
from repositories.models import Repositories


def CREATE_BOOKMARK(user_id: int, repo_id: int) -> str:
    if not UserModel.objects.filter(id=user_id).exists():
        return "User is None"
    if not Repositories.objects.filter(id=repo_id).exists():
        return "Repository is None"
    Bookmark.objects.create(
            user_id = user_id,
            repo_id = repo_id
            )
    return "Create Success"