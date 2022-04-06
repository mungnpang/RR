from typing import List

from comment.models import Comment


def read_comments(id: int) -> Comment:
    return list(Comment.objects.filter(repo_id=id, parent_comment_id__isnull=True).select_related("author"))


def read_replys(id: int) -> Comment:
    return list(Comment.objects.filter(repo_id=id, parent_comment_id__isnull=False).select_related("author"))


def read_user_comments(id: int) -> List[Comment]:
    return list(Comment.objects.filter(author_id=id))
