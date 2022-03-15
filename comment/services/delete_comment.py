from comment.models import Comment

def DELETE_COMMENT(comment_id: int)-> str:
    try:
        Comment.objects.filter(id=comment_id).delete()
    except Comment.DoesNotExist:
        return True, "Comment is None"
    return False, "Delete Success"

