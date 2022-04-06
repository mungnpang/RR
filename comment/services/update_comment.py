from comment.models import Comment


def update_comment(comment_id: int, content: str) -> None:
    comment = Comment.objects.get(id=comment_id)
    comment.content = content
    comment.save()
