from comment.models import Comment
from django.db.transaction import atomic

@atomic
def DELETE_COMMENT(comment_id: int)-> str:
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return True, "Comment is None"
    reply = comment.parent_comment_id
    comment.delete()
    if reply:
        reply_parent = Comment.objects.get(id=reply)
        reply_parent.reply -= 1
        reply_parent.save()
            
    
    return False, "Delete Success"

