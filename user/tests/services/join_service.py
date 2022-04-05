import json

from django.test import Client

from user.models import UserModel


class join_service:
    def create_user(email: str, nickname: str) -> UserModel:
        return UserModel.objects.create(username=nickname, email=email)

    def check_to_id_modify(email: str) -> str:
        client = Client()
        return client.post(
            "/api/v1/user/emailcheck",
            json.dumps({"EMAIL": email}),
            content_type="mutlpart_from xform",
        )

    def check_to_pw_modify(password: str) -> str:
        client = Client()
        return client.post(
            "/api/v1/user/passwordcheck",
            json.dumps({"PASSWORD": password}),
            content_type="application/json",
        )

    def check_to_name_modify(nickname: str) -> str:
        client = Client()
        return client.post(
            "/api/v1/user/nicknamecheck",
            json.dumps({"NICKNAME": nickname}),
            content_type="application/json",
        )
