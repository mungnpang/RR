from typing import Optional
from ninja import Schema


class ReadBookmarkResponse(Schema):
    id: Optional[int]
    user_id: Optional[int]
    repo_id: Optional[int]

class CreateBookmarkResponse(Schema):
    message: str

class DeleteBookmarkResponse(Schema):
    message: str