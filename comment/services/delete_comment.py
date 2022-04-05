from django.db.transaction import atomic

from comment.models import Comment


@atomic
def delete_comment(comment_id: int) -> None:
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    reply = comment.parent_comment_id
    if reply:
        reply_parent = Comment.objects.get(id=reply)
        reply_parent.reply -= 1
        reply_parent.save()
