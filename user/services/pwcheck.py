from asgiref.sync import sync_to_async

from user.services.validator import validation


@sync_to_async
def passwordcheck(password: str) -> dict:
    return validation("password", password)
