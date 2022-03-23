from user.models import UserModel
from asgiref.sync import sync_to_async
from user.services.validator import validation

@sync_to_async
def IDCHECK(email: str) -> str:
    check = UserModel.objects.filter(email=email).exists()
    valid, msg = validation("email", email)
    if not check and valid:
        return "success", msg
    if check:
        return "failed", "이미 가입되어있는 EMAIL입니다."
    return "failed", msg
