from typing import List, Optional

from ninja.errors import HttpError

from comment.models import Comment


def create_comment(content: str, author_id: int, repo_id: int, parent_id: int) -> Comment:
    if not content or not author_id or not repo_id:
        raise HttpError(404, "Empty Space")
    return Comment.objects.create(
        content=content,
        author_id=author_id,
        repo_id=repo_id,
        parent_comment_id=parent_id,
    )


def read_comment(repo_id: int) -> List[Comment]:
    return list(Comment.objects.filter(repo_id=repo_id))


def update_comment(comment_id: int, content: str) -> None:
    if content == "" or content is None:
        raise HttpError(404, "Comment is Empty")
    comment = Comment.objects.get(id=comment_id)
    comment.content = content
    comment.save()


def delete_comment(comment_id: int) -> None:
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
