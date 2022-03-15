from user.models import UserModel
from asgiref.sync import sync_to_async
from user.services.validator import validation

@sync_to_async
def NAMECHECK(nickname: str) -> str:
    check = UserModel.objects.filter(nickname=nickname)
    valid, msg = validation("nickname", nickname)
    if len(check) == 0 and valid:
        return "success", msg
    if len(check) > 0:
        return "failed", "이미 가입된 닉네임입니다."
    return "failed", msg