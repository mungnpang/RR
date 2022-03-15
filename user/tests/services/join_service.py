from django.db import transaction
from user.models import UserModel
from django.test import Client
import json

class join_service:

    @transaction.atomic
    def create_user(email: str, nickname: str) -> UserModel:
        user = UserModel.objects.create(nickname = nickname, email = email)
        return user

    def check_to_id_modify(email: str) -> str:
        client = Client()
        response = client.post('/api/v1/user/emailcheck', json.dumps({"EMAIL":email}), content_type="application/json")
        return response

    def check_to_pw_modify(password: str) -> str:
        client = Client()
        response = client.post('/api/v1/user/passwordcheck', json.dumps({"PASSWORD":password}), content_type="application/json")
        return response

    def check_to_name_modify(nickname: str) -> str:
        client = Client()
        response = client.post('/api/v1/user/nicknamecheck', json.dumps({"NICKNAME":nickname}), content_type="application/json")
        return response

