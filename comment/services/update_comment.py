from comment.models import Comment

def COMMENT_UPDATE(comment_id: int, content: str) -> str:
    if content == '':
        return True, "Empty Space"
    try:
        comment = Comment.objects.get(id = comment_id)
        comment.content = content
        comment.save()
    except Comment.DoesNotExist:
        return "Comment is None"
    return "Update Success"