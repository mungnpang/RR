from django.http import HttpRequest, JsonResponse, response
from ninja import Router
from ninja.errors import HttpError

from user.API.V1.schemas import (
    IdCheckRequest,
    IdCheckResponse,
    NickNameCheckRequest,
    NickNameCheckResponse,
    PassWordCheckRequest,
    PassWordCheckResponse,
    EmailDBResponse,
    EmailDBCheckRequest,
)
from user.services import idcheck, namecheck, passwordcheck, email_in_db_check
from user.models import UserModel

router = Router(tags=["user"])


@router.post("/emailcheck", response={200: IdCheckResponse})
async def check_to_id(request: HttpRequest, id_check_request: IdCheckRequest) -> dict:
    db_in, result, message = await idcheck(id_check_request.EMAIL)
    if not db_in and result:
        return JsonResponse({"result": result, "message": message})
    elif db_in:
        raise HttpError(422, "이미 가입된 이메일입니다.")
    else:
        raise HttpError(422, message)


@router.post("/password1check", response={200: PassWordCheckResponse})
async def check_to_pw(
    request: HttpRequest, pw_check_request: PassWordCheckRequest
) -> dict:
    result, message = await passwordcheck(pw_check_request.PASSWORD1)
    if result:
        return JsonResponse({"result": result, "message": message})
    else:
        raise HttpError(422, message)


@router.post("/usernamecheck", response={200: NickNameCheckResponse})
async def check_to_nickname(
    request: HttpRequest, nickname_check_requests: NickNameCheckRequest
) -> dict:
    db_in, result, message = await namecheck(nickname_check_requests.USERNAME)
    if not db_in and result:
        return JsonResponse({"result": result, "message": message})
    elif db_in:
        raise HttpError(422, "이미 가입된 닉네임입니다.")
    else:
        raise HttpError(422, message)


@router.post("/email_db_check", response={200: EmailDBResponse})
async def check_to_email_in_db(
    request: HttpRequest, email_check_request: EmailDBCheckRequest
) -> dict:
    try:
        await email_in_db_check(email_check_request.EMAIL)
    except UserModel.DoesNotExist:
        raise HttpError(404, "존재하지 않는 이메일입니다.")
    else:
        return JsonResponse({"result": "success"})
