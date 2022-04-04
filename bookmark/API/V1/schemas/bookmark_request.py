from ninja import Schema

class CreateBookmarkRequest(Schema):
    REPO_ID: int

class DeleteBookmarkRequest(Schema):
    REPO_ID: int

