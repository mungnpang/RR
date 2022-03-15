from bookmark.models import Bookmark

def DELETE_BOOKMARK(user_id:int, repo_id:int ) -> str:
    Bookmark.objects.filter(user_id=user_id, repo_id=repo_id).delete()
    return "Delete Success"