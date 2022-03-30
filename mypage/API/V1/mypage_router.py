from typing import List
from django.http import HttpRequest
from ninja import Router
from mypage.API.V1.schemas import (
    Create_History_Request,
    Read_Reponse
    )

from mypage.services import CREATE_HISTORY, READ_HISTORY

router = Router(tags=["mypage"])

@router.post('/create/', response = None)
def Create_History(request: HttpRequest, create_history_request: Create_History_Request) -> None:
    recommand_list = create_history_request.RECOMMAND
    repo_id = create_history_request.REPOSITORY
    user = request.user.id
    CREATE_HISTORY(user, repo_id, recommand_list)

@router.get('/read/{user}', response={200: Read_Reponse})
def Read_History(request: HttpRequest, user: int) -> dict:
    return READ_HISTORY(user)

    
    