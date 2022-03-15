from comment.models import Comment

def COMMENTS_READ(repo_id: int, ) -> Comment:
    return list(Comment.objects.filter(repo_id=repo_id))
    

