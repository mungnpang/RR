from typing import List

from ninja.errors import HttpError

from bookmark.models import Bookmark
from repositories.models import Repositories
from user.models import UserModel


def create_bookmark(user_id: int, repo_id: int) -> None:
    if not UserModel.objects.filter(id=user_id).exists():
        raise HttpError(404, "User Not Found")
    if not Repositories.objects.filter(id=repo_id).exists():
        raise HttpError(404, "Repository Not Found")
    Bookmark.objects.create(
        user_id=user_id,
        repo_id=repo_id,
    )


def read_bookmark(user_id: int) -> List[Bookmark]:
    if not UserModel.objects.filter(id=user_id).exists():
        raise HttpError(404, "User Not Found")
    return list(Bookmark.objects.filter(user_id=user_id))


def delete_bookmark(user_id: int, repo_id: int) -> None:
    if not UserModel.objects.filter(id=user_id).exists():
        raise HttpError(404, "User Not Found")
    if not Repositories.objects.filter(id=repo_id).exists():
        raise HttpError(404, "Repository Not Found")
    delete = Bookmark.objects.filter(user_id=user_id, repo_id=repo_id)
    if not delete.exists():
        raise HttpError(404, "Bookmark Not Found")
    delete.delete()
