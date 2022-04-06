from typing import Optional

from ninja import Schema
from pydantic import BaseModel, validator


class CommentsRequest(Schema):
    REPO_ID: int


class CreateCommentRequest(Schema):
    REPO_ID: int
    CONTENT: str
    PARENT_COMMENT_ID: Optional[int]


class UpdateCommentRequest(BaseModel):
    COMMENT_ID: int
    CONTENT: str

    @validator("CONTENT")
    def content_must_not_empty(cls, v: str):
        if v.isspace() or not v:
            raise ValueError("Empty Space")
        return v


class DeleteCommentRequest(Schema):
    COMMENT_ID: int
