from typing import List
from urllib.error import HTTPError

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from ninja import Router

from bookmark.API.V1.schemas import (
    CreateBookmarkRequest,
    CreateBookmarkResponse,
    DeleteBookmarkRequest,
    DeleteBookmarkResponse,
    ReadBookmarkResponse,
)
from bookmark.models import Bookmark
from bookmark.services import (
    create_bookmark,
    delete_bookmark,
    read_bookmark,
    read_get_bookmark,
)

router = Router(tags=["Bookmark"])


@login_required(login_url="/accounts/login")
@router.get("/read/{user_id}", response={200: List[ReadBookmarkResponse]})
def bookmark_read(request: HttpRequest, user_id: int) -> List[Bookmark]:
    bookmark = read_bookmark(user_id)
    if len(bookmark) == 0:
        raise HTTPError(404, "Bookmark is None")
    return bookmark


@login_required(login_url="/accounts/login")
@router.get("/read_get_one/{repo_id}", response={200: ReadBookmarkResponse})
def read_get_one_bookmark(request: HttpRequest, repo_id: int) -> Bookmark:
    user = request.user.id
    bookmark = read_get_bookmark(user, repo_id)
    if len(bookmark) == 0:
        raise HTTPError(404, "Bookmark is None")
    return JsonResponse({"result": "success"}, status=200)


@login_required(login_url="/accounts/login")
@router.post("/create/", response={201: CreateBookmarkResponse})
def bookmark_create(
    request: HttpRequest, create_bookmark_request: CreateBookmarkRequest
) -> dict:
    user = request.user.id
    bookmark = create_bookmark(user, create_bookmark_request.REPO_ID)
    if bookmark:
        return JsonResponse({"result": "success"}, status=201)
    raise HTTPError(404, "User or Repository is None")


@login_required(login_url="/accounts/login")
@router.delete("/delete", response={201: DeleteBookmarkResponse})
def bookmark_delete(
    request: HttpRequest, delete_bookmark_request: DeleteBookmarkRequest
) -> dict:
    user = request.user.id
    try:
        delete_bookmark(user, delete_bookmark_request.REPO_ID)
    except Bookmark.DoesNotExist:
        raise HTTPError(404, "Bookmark is None")
    return JsonResponse({"result": "success"}, status=201)
