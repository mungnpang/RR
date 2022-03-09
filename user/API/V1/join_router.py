from typing import Tuple
from django.http import HttpRequest, response ,JsonResponse
from ninja import Router
from ninja.errors import HttpError
from user.API.V1.schemas import JoinRequest, JoinResponse, IdCheckRequest, IdCheckResponse
from user.services import IDCHECK

router = Router(tags=["user"])

@router.post("/idcheck", response={201: IdCheckResponse})
async def check_to_id(request: HttpRequest, id_check_request: IdCheckRequest) -> dict:
    result = await IDCHECK(id_check_request.EMAIL)
    return {"result":result}

