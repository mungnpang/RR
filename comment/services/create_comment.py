from typing import Optional

from comment.models import Comment


class CreateCommentRequest:
    author: int
    repo_id: int
    content: str
    parent_comment_id: Optional[int]


def create_comment(CreateCommentRequest) -> None:
    Comment.objects.create(
        author_id=CreateCommentRequest.author,
        repo_id=CreateCommentRequest.repo_id,
        content=CreateCommentRequest.content,
        parent_comment_id=CreateCommentRequest.parent_comment_id,
    )
    if CreateCommentRequest.parent_comment_id is not None:
        comment = Comment.objects.get(id=CreateCommentRequest.parent_comment_id)
        comment.reply += 1
        comment.save()
