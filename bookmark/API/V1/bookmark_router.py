from typing import List
from django.http import HttpRequest, JsonResponse
from ninja import Router
from bookmark.API.V1.schemas import (
    CreateBookmarkRequest,
    CreateBookmarkResponse,
    ReadBookmarkResponse,
    DeleteBookmarkRequest,
    DeleteBookmarkResponse
)

from django.contrib.auth.decorators import login_required
from bookmark.services import CREATE_BOOKMARK, READ_BOOKMARK, DELETE_BOOKMARK
from bookmark.models import Bookmark

router = Router(tags=["Bookmark"])

@router.get('/read/<str:user_id>', response={200: List[ReadBookmarkResponse]})
def read_bookmark(request: HttpRequest, user_id: str) -> List[Bookmark]:
    bookmark = READ_BOOKMARK(int(user_id))
    return bookmark

@login_required
@router.post('/create', response={201:CreateBookmarkResponse})
def create_bookmark(request: HttpRequest, create_bookmark_request: CreateBookmarkRequest) -> str:
    bookmark = CREATE_BOOKMARK(create_bookmark_request.USER_ID, create_bookmark_request.REPO_ID)
    return JsonResponse({"message" : bookmark})

@login_required
@router.delete('/delete', response={201:DeleteBookmarkResponse})
def delete_bookmark(request: HttpRequest, delete_bookmark_request: DeleteBookmarkRequest) -> str:
    bookmark =  DELETE_BOOKMARK(delete_bookmark_request.USER_ID, delete_bookmark_request.REPO_ID)
    return JsonResponse({"mesaage": bookmark})