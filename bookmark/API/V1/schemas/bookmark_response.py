from typing import Optional
from ninja import Schema
from repositories.API.V1.schemas import ReadRepoResponse


class ReadBookmarkResponse(Schema):
    repo: ReadRepoResponse
    

class CreateBookmarkResponse(Schema):
    message: str

class DeleteBookmarkResponse(Schema):
    message: str