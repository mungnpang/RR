from typing import List
from comment.models import Comment

def COMMENTS_READ(id: int) -> Comment:
    return list(Comment.objects.filter(repo_id=id, parent_comment_id__isnull=True).select_related('author'))

def REPLYS_READ(id: int) -> Comment:
    return list(Comment.objects.filter(repo_id=id, parent_comment_id__isnull=False).select_related('author'))

def COMMENTS_READ_USER(id: int) -> List[Comment]:
    return list(Comment.objects.filter(author_id=id))
