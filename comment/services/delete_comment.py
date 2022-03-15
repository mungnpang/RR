from comment.models import Comment

def DELETE_COMMENT(comment_id: int)-> None:
    Comment.objects.filter(id=comment_id).delete()

