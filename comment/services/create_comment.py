from typing import Optional
from django.http import HttpRequest
from comment.models import Comment
from django.db import transaction
from django.db.utils import IntegrityError

def COMMENTS_CREATE(author:int, repo_id:int, content: str, parent_comment_id: Optional[int]) -> str:
    try:
        with transaction.atomic():
            Comment.objects.create(
                author_id = author,
                repo_id = repo_id,
                content=content,
                parent_comment_id = parent_comment_id,
            )
    except IntegrityError:
            return True, "Empty Space"
    return False, "Create Success"