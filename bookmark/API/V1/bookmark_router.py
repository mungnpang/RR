from os import stat
from typing import List
from django.http import HttpRequest, HttpResponse, JsonResponse
from ninja import Router
from bookmark.API.V1.schemas import (
    CreateBookmarkRequest,
    CreateBookmarkResponse,
    ReadBookmarkResponse,
    DeleteBookmarkRequest,
    DeleteBookmarkResponse
)

from django.contrib.auth.decorators import login_required
from bookmark.services import CREATE_BOOKMARK, READ_BOOKMARK, DELETE_BOOKMARK, READ_GET_BOOKMARK
from bookmark.models import Bookmark

router = Router(tags=["Bookmark"])

@router.get('/read/{user_id}', response={200: List[ReadBookmarkResponse]})
def read_bookmark(request: HttpRequest, user_id: int) -> List[Bookmark]:
    bookmark = READ_BOOKMARK(user_id)
    if len(bookmark) == 0:
        return JsonResponse({"result":"failed","message":"Bookmark is None"}, status=422)
    return bookmark

@router.get('/read_get_one/{repo_id}', response={200: ReadBookmarkResponse})
def read_get_one_bookmark(request: HttpRequest, repo_id: int) -> Bookmark:
    user = request.user.id
    bookmark = READ_GET_BOOKMARK(user, repo_id)
    if len(bookmark) == 0:
        return JsonResponse({"result":"failed","message":"Bookmark is None"})
    return JsonResponse({"result":"success"}, status=200)

@login_required
@router.post('/create/', response={201:CreateBookmarkResponse})
def create_bookmark(request: HttpRequest, create_bookmark_request: CreateBookmarkRequest) -> str:
    user = request.user.id
    result, message = CREATE_BOOKMARK(user, create_bookmark_request.REPO_ID)
    if result:
        return JsonResponse({"result":"failed","message" : message}, status=422)
    return JsonResponse({"result":"success","message" : message}, status=201)

@login_required
@router.delete('/delete', response={201:DeleteBookmarkResponse})
def delete_bookmark(request: HttpRequest, delete_bookmark_request: DeleteBookmarkRequest) -> str:
    user = request.user.id
    result, message =  DELETE_BOOKMARK(user, delete_bookmark_request.REPO_ID)
    if result:
        return JsonResponse({"result":"failed", "message":message}, status=422)
    return JsonResponse({"result":"success", "message": message}, status=201)


