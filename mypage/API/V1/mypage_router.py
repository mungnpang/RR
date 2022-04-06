from typing import List

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from ninja import Router
from ninja.errors import HttpError

from mypage.API.V1.schemas import (
    Create_History_Recommand_Request,
    Create_History_Repository_Request,
    Read_Reponse,
)
from mypage.models import Mypage
from mypage.services import (
    create_history_repository,
    create_history_recocommand,
    read_history,
)

router = Router(tags=["mypage"])


@login_required(login_url="/accounts/login")
@router.post("/create/repo", response=None)
def create_user_history(
    request: HttpRequest, create_history_request: Create_History_Repository_Request
) -> None:
    user = request.user.id
    create_history_repository(user, create_history_request.REPOSITORY)


@login_required(login_url="/accounts/login")
@router.post("/create/reco", response=None)
def create_user_history(
    request: HttpRequest, create_history_request: Create_History_Recommand_Request
) -> None:
    user = request.user.id
    create_history_recocommand(user, create_history_request.RECOMMAND)


@login_required(login_url="/accounts/login")
@router.get("/read/{user}", response={200: Read_Reponse})
def read_user_history(request: HttpRequest, user: int) -> dict:
    try:
        user_info = read_history(user)
    except Mypage.DoesNotExist:
        raise HttpError(404, "User Not Found")
    return JsonResponse(
        {
            "repo_history": user_info.recently_visit,
            "reco_history": user_info.recently_recommand,
        }
    )
