from ninja import Schema

class BookmarkReponse(Schema):
    ID: int
    USER_ID: int
    REPO_ID: int