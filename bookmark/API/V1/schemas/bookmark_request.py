from ninja import Schema

class CreateBookmarkRequest(Schema):
    USER_ID: int
    REPO_ID: int

class DeleteBookmarkRequest(Schema):
    USER_ID: int
    REPO_ID: int

