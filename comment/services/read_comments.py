from comment.models import Comment

def COMMENTS_READ(repo_id: int, ) -> Comment:
    comments = Comment.objects.filter(repo_id=repo_id)
    return comments