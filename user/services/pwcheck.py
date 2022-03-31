from asgiref.sync import sync_to_async
from user.services.validator import validation

@sync_to_async
def PASSWORDCHECK(password: str) -> dict:
    valid, msg = validation("password", password)
    if valid:
        return "success", msg
    return "failed", msg