from bookmark.models import Bookmark


def delete_bookmark(user_id: int, repo_id: int) -> None:
    bookmark = Bookmark.objects.get(user_id=user_id, repo_id=repo_id)
    bookmark.delete()
