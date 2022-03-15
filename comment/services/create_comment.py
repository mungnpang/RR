from django.http import HttpRequest
from comment.models import Comment

def COMMENTS_CREATE(request:HttpRequest, repo_id:int, content: str, parent_comment_id: str) -> str:
    
    author = request.user
    Comment.objects.create(
        author_id = author,
        repo_id = repo_id,
        content=content,
        parent_comment_id = parent_comment_id,
    )