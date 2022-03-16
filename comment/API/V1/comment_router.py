from typing import List
from django.http import HttpRequest, JsonResponse, response
from ninja import Router
from comment.API.V1.schemas import (
    CommentsResponse,
    CreateCommentRequest,
    CreateCommentResponse,
    UpdateCommentRequest,
    UpdateCommentResponse,
    DeleteCommentRequest,
    DeleteCommentResponse,
)
from comment.models import Comment
from comment.services import COMMENTS_READ, COMMENTS_CREATE, COMMENT_UPDATE, DELETE_COMMENT
from django.contrib.auth.decorators import login_required

router = Router(tags=["comment"])

@router.get("/read/{repo}", response={200: List[CommentsResponse]})
def comment_read(request: HttpRequest, repo: str) -> List[Comment]:
    comments = COMMENTS_READ(int(repo))
    if len(comments) == 0:
        return JsonResponse({"result":"failed", "message" : "Data is None"}, status=422)
    return comments

@login_required
@router.post('/create/', response={201:CreateCommentResponse})
def comment_create(request: HttpRequest, create_comment_request: CreateCommentRequest) -> dict:
    # result, message = COMMENTS_CREATE(request.user, create_comment_request.REPO_ID,create_comment_request.CONTENT, create_comment_request.PARENT_COMMENT_ID)
    result, message = COMMENTS_CREATE(create_comment_request.USER_ID, create_comment_request.REPO_ID,create_comment_request.CONTENT, create_comment_request.PARENT_COMMENT_ID)
    if result:
        return JsonResponse({"result":"failed","message" : message}, status=422)
    return JsonResponse({"result":"success","message" : message}, status=201)

@login_required
@router.put('/update', response={201:UpdateCommentResponse})
def comment_update(request: HttpRequest, update_comment_request: UpdateCommentRequest) -> dict:
    result, message = COMMENT_UPDATE(update_comment_request.COMMENT_ID, update_comment_request.CONTENT)
    if result:
        return JsonResponse({"result":"failed","message" : message}, status=422)
    return JsonResponse({"result":"success","message" : message}, status=201)

@login_required
@router.delete('/delete', response={201:DeleteCommentResponse})
def comment_delete(request:HttpRequest, delete_comment_request: DeleteCommentRequest) -> dict:
    result, message = DELETE_COMMENT(delete_comment_request.COMMENT_ID)
    if result:
        return JsonResponse({"result":"failed","message" : message}, status=422)
    return JsonResponse({"result":"success","message" : message}, status=201)