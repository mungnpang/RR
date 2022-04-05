from typing import List

from bookmark.models import Bookmark
from repositories.models import Repositories
from user.models import UserModel


def Create_Bookmark(user_id: int, repo_id: int) -> Bookmark:
    if not UserModel.objects.filter(id=user_id).exists():
        return "User is None"
    if not Repositories.objects.filter(id=repo_id).exists():
        return "Repository is None"
    return Bookmark.objects.create(
        user_id=user_id,
        repo_id=repo_id,
    )


def Read_Bookmark(user_id: int) -> List[Bookmark]:
    if not UserModel.objects.filter(id=user_id).exists():
        return "User is None"
    return list(Bookmark.objects.filter(user_id=user_id))


def Delete_BookMark(user_id: int, repo_id: int) -> str:
    if not UserModel.objects.filter(id=user_id).exists():
        return "User is None"
    if not Repositories.objects.filter(id=repo_id).exists():
        return "Repository is None"
    delete = Bookmark.objects.filter(user_id=user_id, repo_id=repo_id)
    if not delete.exists():
        return "Bookmark is None"
    delete.delete()
    return "Delete Success"
