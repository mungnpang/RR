from comment.models import Comment


def update_comment(comment_id: int, content: str) -> bool:
    if content == "":
        return False
    comment = Comment.objects.get(id=comment_id)
    comment.content = content
    comment.save()
    return True, "Update Success"
