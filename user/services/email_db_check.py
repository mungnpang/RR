from asgiref.sync import sync_to_async
from user.models import UserModel


@sync_to_async
def email_in_db_check(email: str) -> UserModel:
    return UserModel.objects.get(email=email)
