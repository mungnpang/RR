from comment.models import Comment

def DELETE_COMMENT(comment_id: int)-> str:
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return True, "Comment is None"
    comment.delete()
    return False, "Delete Success"

