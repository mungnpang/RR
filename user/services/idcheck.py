from posixpath import split
from user.models import UserModel
from asgiref.sync import sync_to_async
import re

domain = ["com","kr","net","org","biz","info"]

def modify_email(email):
    if (re.search('[^a-zA-Z0-9-_.@]+', email)) is not None or not (14 < len(email) < 35) or email.split('.')[-1] not in domain:
        return False
    return True

@sync_to_async
def IDCHECK(email: str) -> dict:
    check = UserModel.objects.filter(email=email)
    if len(check) or not modify_email(email):
        return "failed"
    return "success"
