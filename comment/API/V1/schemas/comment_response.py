from datetime import datetime
from typing import Optional
from ninja import Schema
from user.API.V1.schemas.join_response import UserNameResponse

class CommentsResponse(Schema):
    id: int
    content: str
    author: UserNameResponse
    parent_comment_id: Optional[int]
    message: Optional[str]
    result: Optional[str]
    created_at: datetime
    reply: int
    repo_id: int
    

class CreateCommentResponse(Schema):
    message: str

class UpdateCommentResponse(Schema):
    message: str 

class DeleteCommentResponse(Schema):
    message: str 