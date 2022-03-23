from user.models import UserModel
from asgiref.sync import sync_to_async
from user.services.validator import validation


@sync_to_async
def NAMECHECK(nickname: str) -> str:
    check = UserModel.objects.filter(username=nickname).exists()
    valid, msg = validation("nickname", nickname)
    if not check and valid:
        return "success", msg
    if check:
        return "failed", "이미 가입된 닉네임입니다."
    return "failed", msg