from django.http import HttpRequest, JsonResponse
from ninja import Router
from user.API.V1.schemas import (
    IdCheckRequest, 
    IdCheckResponse,
    PassWordCheckRequest,
    PassWordCheckResponse, 
    NickNameCheckRequest,
    NickNameCheckResponse
)

from user.services import IDCHECK, NAMECHECK, PASSWORDCHECK

router = Router(tags=["user"])

@router.post("/emailcheck", response={200: IdCheckResponse})
async def check_to_id(request: HttpRequest, id_check_request: IdCheckRequest) -> dict:
    result, msg = await IDCHECK(id_check_request.EMAIL)
    data = {
        "result" : result,
        "msg" : msg
    }
    return JsonResponse(data)

@router.post("/passwordcheck", response={200:PassWordCheckResponse})
async def check_to_pw(request: HttpRequest, pw_check_request: PassWordCheckRequest) -> dict:
    result, msg = await PASSWORDCHECK(pw_check_request.PASSWORD)
    data = {
        "result" : result,
        "msg" : msg
    }
    return JsonResponse(data)

@router.post("/nicknamecheck", response={200: NickNameCheckResponse})
async def check_to_nickname(request: HttpRequest, nickname_check_requests: NickNameCheckRequest) -> dict:
    result, msg = await NAMECHECK(nickname_check_requests.NICKNAME)
    data = {
        "result" : result,
        "msg" : msg
    }
    return JsonResponse(data)
