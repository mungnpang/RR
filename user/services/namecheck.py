from asgiref.sync import sync_to_async

from user.models import UserModel
from user.services.validator import validation


@sync_to_async
def namecheck(nickname: str) -> str:
    check = UserModel.objects.filter(username=nickname).exists()
    valid, msg = validation("nickname", nickname)
    return check, valid, msg
