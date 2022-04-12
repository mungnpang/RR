from comment.models import Comment
from ninja.errors import HttpError


def update_comment(user: str, comment_id: int, content: str) -> None:
    comment = Comment.objects.get(id=comment_id)
    if user == comment.author:
        comment.content = content
        comment.save()
        return
    raise HttpError(422, "작성자가 아닙니다.")
