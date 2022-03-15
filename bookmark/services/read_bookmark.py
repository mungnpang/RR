from typing import List
from bookmark.models import Bookmark

def READ_BOOKMARK(user_id: int) -> List[Bookmark]:
    return list(Bookmark.objects.filter(user_id=user_id).order_by('-id'))