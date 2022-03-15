from ninja import Schema

class BookmarkRequest(Schema):
    USER_ID: int
    REPO_ID: int