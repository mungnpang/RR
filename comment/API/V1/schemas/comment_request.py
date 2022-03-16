from typing import Optional
from ninja import Schema
from user.models import UserModel


class CommentsRequest(Schema):
    REPO_ID: int

class CreateCommentRequest(Schema):
    USER_ID: int
    REPO_ID: int
    CONTENT: str
    PARENT_COMMENT_ID: Optional[int]

class UpdateCommentRequest(Schema):
    COMMENT_ID: int
    CONTENT: str

class DeleteCommentRequest(Schema):
    COMMENT_ID: int
    
