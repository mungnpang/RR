from typing import List, Optional

from django.db import transaction
from django.db.utils import IntegrityError

from comment.models import Comment


def Create_Comment(content: str, author_id: int, repo_id: int, parent_id: int) -> Comment:
    try:
        with transaction.atomic():
            comment = Comment.objects.create(
                content=content,
                author_id=author_id,
                repo_id=repo_id,
                parent_comment_id=parent_id,
            )
    except IntegrityError:
        return "Empty Space"
    return comment


def Read_Comment(repo_id: int) -> List[Comment]:
    comments = list(Comment.objects.filter(repo_id=repo_id))
    if comments == []:
        return "Data is None"
    return list(comments)


def Update_Comment(comment_id: int, content: str) -> Comment:
    if content == "" or content is None:
        return "Comment is Empty"
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return "Comment is None"
    else:
        comment.content = content
        comment.save()
    return comment


def Delete_Comment(comment_id: int) -> str:
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return "Comment is None"
    else:
        comment.delete()
    return "Delete Success"
