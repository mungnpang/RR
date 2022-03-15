from comment.models import Comment

def COMMENT_UPDATE(comment_id: int, content: str) -> None:
    comment = Comment.objects.get(id = comment_id)
    comment.content = content
    comment.save()