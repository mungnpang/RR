from typing import List
from bookmark.models import Bookmark

def READ_BOOKMARK(user_id: int) -> List[Bookmark]:
    return list(Bookmark.objects.filter(user_id=user_id).select_related('repo').order_by('-id'))
def READ_GET_BOOKMARK(user_id:int, repo_id: int) -> Bookmark:
    return list(Bookmark.objects.filter(user_id=user_id, repo_id=repo_id))