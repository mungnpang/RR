from typing import Optional

from comment.models import Comment
from comment.API.V1.schemas import CreateCommentRequest


def create_comment(author: int, CreateCommentRequest) -> None:
    Comment.objects.create(
        author_id=author,
        repo_id=CreateCommentRequest.REPO_ID,
        content=CreateCommentRequest.CONTENT,
        parent_comment_id=CreateCommentRequest.PARENT_COMMENT_ID,
    )
    if CreateCommentRequest.PARENT_COMMENT_ID is not None:
        comment = Comment.objects.get(id=CreateCommentRequest.PARENT_COMMENT_ID)
        comment.reply += 1
        comment.save()
