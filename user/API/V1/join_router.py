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
    result, message = await IDCHECK(id_check_request.EMAIL)
    data = {
        "result" : result,
        "message" : message
    }
    return JsonResponse(data)

@router.post("/password1check", response={200:PassWordCheckResponse})
async def check_to_pw(request: HttpRequest, pw_check_request: PassWordCheckRequest) -> dict:
    result, message = await PASSWORDCHECK(pw_check_request.PASSWORD1)
    data = {
        "result" : result,
        "message" : message
    }
    return JsonResponse(data)

@router.post("/usernamecheck", response={200: NickNameCheckResponse})
async def check_to_nickname(request: HttpRequest, nickname_check_requests: NickNameCheckRequest) -> dict:
    result, message = await NAMECHECK(nickname_check_requests.USERNAME)
    data = {
        "result" : result,
        "message" : message
    }
    return JsonResponse(data)
