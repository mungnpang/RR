from bookmark.models import Bookmark

def DELETE_BOOKMARK(user_id:int, repo_id:int ) -> str:
    try:
        bookmark = Bookmark.objects.get(user_id=user_id, repo_id=repo_id)
    except Bookmark.DoesNotExist:
        return True, "Bookmark is None"
    bookmark.delete()
    return False, "Delete Success"