from typing import List

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from ninja import Router
from ninja.errors import HttpError

from mypage.API.V1.schemas import Create_History_Request, Read_Reponse
from mypage.models import Mypage
from mypage.services import create_history, read_history

router = Router(tags=["mypage"])


@login_required(login_url="/accounts/login")
@router.post("/create/", response=None)
def create_user_history(request: HttpRequest, create_history_request: Create_History_Request) -> None:
    recommand_list = create_history_request.RECOMMAND
    repo_id = create_history_request.REPOSITORY
    user = request.user.id
    create_history(user, repo_id, recommand_list)


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
