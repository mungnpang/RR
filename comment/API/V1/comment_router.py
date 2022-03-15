from django.http import HttpRequest, JsonResponse, response
from ninja import Router
from comment.API.V1.schemas import (
    CommentsRequest,
    CommentsResponse,
    CreateCommentRequest,
    CreateCommentResponse,
    UpdateCommentRequest,
    UpdateCommentResponse,
    DeleteCommentRequest,
    DeleteCommentResponse
)
from comment.services import COMMENTS_READ, COMMENTS_CREATE, COMMENT_UPDATE, DELETE_COMMENT
from django.contrib.auth.decorators import login_required

router = Router(tags=["comment"])

@router.get("/", response={200: CommentsResponse})
def comment_read(request: HttpRequest, comment_request:CommentsRequest) -> dict:
    comments = COMMENTS_READ(comment_request.REPO_ID)
    result = {'result':comments}
    return JsonResponse(result)

@login_required
@router.post('/create', response={201:CreateCommentResponse})
def comment_create(request: HttpRequest, create_comment_request: CreateCommentRequest) -> dict:
    create = COMMENTS_CREATE(request, create_comment_request.REPO_ID,create_comment_request.CONTENT, create_comment_request.PARENT_COMMENT_ID)
    return JsonResponse(message="created comment")

@login_required
@router.put('/update', response={201:UpdateCommentResponse})
def comment_update(request: HttpRequest, update_comment_request: UpdateCommentRequest) -> dict:
    update = COMMENT_UPDATE(update_comment_request.COMMENT_ID, update_comment_request.CONTENT)
    return JsonResponse(message="updated comment")

@login_required
@router.delete('/delete', response={201:DeleteCommentResponse})
def comment_delete(request:HttpRequest, delete_comment_request: DeleteCommentRequest) -> dict:
    delete = DELETE_COMMENT(DeleteCommentRequest.COMMENT_ID)
    return JsonResponse(message="deleted comment")