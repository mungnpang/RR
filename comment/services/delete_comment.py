from django.db.transaction import atomic

from comment.models import Comment
from ninja.errors import HttpError


@atomic
def delete_comment(user: str, comment_id: int) -> None:
    comment = Comment.objects.get(id=comment_id)
    if user == comment.author:
        comment.delete()
        reply = comment.parent_comment_id
        if reply:
            reply_parent = Comment.objects.get(id=reply)
            reply_parent.reply -= 1
            reply_parent.save()
        return
    raise HttpError(422, "작성자가 아닙니다.")
