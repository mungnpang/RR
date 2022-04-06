from typing import Union

from asgiref.sync import sync_to_async

from user.models import UserModel
from user.services.validator import validation


@sync_to_async
def idcheck(email: str) -> Union[str, str]:
    check = UserModel.objects.filter(email=email).exists()
    valid, msg = validation("email", email)
    return check, valid, msg
