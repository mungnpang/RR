from typing import Any, List

from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.http import HttpRequest, HttpResponse, JsonResponse, response
from ninja import Router
from ninja.errors import HttpError

from comment.API.V1.schemas import (
    CommentsResponse,
    CreateCommentRequest,
    CreateCommentResponse,
    DeleteCommentRequest,
    DeleteCommentResponse,
    UpdateCommentRequest,
    UpdateCommentResponse,
)
from comment.models import Comment
from comment.services import (
    create_comment,
    delete_comment,
    read_comments,
    read_replys,
    read_user_comments,
    update_comment,
)

router = Router(tags=["comment"])


@router.get("/read_user/{user}", response={200: List[CommentsResponse]})
def comment_read_user(request: HttpRequest, user: int) -> List[Comment]:
    comments = read_user_comments(user)
    if len(comments) == 0:
        raise HttpError(404, "Comment is None")
    return comments


@router.get("/read/{repo}", response={200: List[CommentsResponse]})
def comment_read(request: HttpRequest, repo: str) -> List[Comment]:
    comments = read_comments(int(repo))
    if len(comments) == 0:
        raise HttpError(404, "Comment is None")
    return comments


@router.get("/read_reply/{repo}", response={200: List[CommentsResponse]})
def comment_reply_read(request: HttpRequest, repo: str) -> List[Comment]:
    replys = read_replys(int(repo))
    if len(replys) == 0:
        raise HttpError(404, "Comment is None")
    return replys


@login_required(login_url="/accounts/login")
@router.post("/create/", response={201: CreateCommentResponse})
def comment_create(
    request: HttpRequest, create_comment_request: CreateCommentRequest
) -> dict:
    user_id = request.user.id
    try:
        create_comment(
            user_id,
            create_comment_request,
        )
    except IntegrityError:
        raise HttpError(422, "Empty Space")
    return JsonResponse({"result": "success"}, status=201)


@login_required(login_url="/accounts/login")
@router.put("/update", response={201: UpdateCommentResponse})
def comment_update(
    request: HttpRequest, update_comment_request: UpdateCommentRequest
) -> dict:
    try:
        update_comment(
            request.user,
            update_comment_request.COMMENT_ID,
            update_comment_request.CONTENT,
        )
    except Comment.DoesNotExist:
        raise HttpError(404, "Comment is None")
    return JsonResponse({"result": "success"}, status=201)


@login_required(login_url="/accounts/login")
@router.delete("/delete", response={201: DeleteCommentResponse})
def comment_delete(
    request: HttpRequest, delete_comment_request: DeleteCommentRequest
) -> dict:
    try:
        delete_comment(request.user, delete_comment_request.COMMENT_ID)
    except Comment.DoesNotExist:
        raise HttpError(404, "Comment is None")
    return JsonResponse({"result": "success"}, status=201)
