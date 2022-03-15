from ninja import Schema

class CommentsResponse(Schema):
    message: str

class CreateCommentResponse(Schema):
    message: str

class UpdateCommentResponse(Schema):
    message: str 

class DeleteCommentResponse(Schema):
    message: str 