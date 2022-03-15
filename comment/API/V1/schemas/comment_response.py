from typing import Optional
from ninja import Schema

class CommentsResponse(Schema):
    content: str
    author_id: int
    parent_comment_id: Optional[int]
    repo_id: int
    message: Optional[str]
    result: Optional[str]

class CreateCommentResponse(Schema):
    message: str

class UpdateCommentResponse(Schema):
    message: str 

class DeleteCommentResponse(Schema):
    message: str 