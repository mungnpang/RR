import json
from typing import Optional

from django.test import Client

from user.models import UserModel


class join_service:
    def create_user(email: str, nickname: str) -> UserModel:
        return UserModel.objects.create(username=nickname, email=email)

    def check_to_id_modify(email: str) -> json:
        client = Client()
        return client.post(
            "/api/v1/user/emailcheck",
            data=json.dumps({"EMAIL": email}),
            content_type="application/json",
        )

    def check_to_pw_modify(password: str) -> json:
        client = Client()
        return client.post(
            "/api/v1/user/password1check",
            data={"PASSWORD1": password},
            content_type="application/json",
        )

    def check_to_name_modify(nickname: str) -> json:
        client = Client()
        return client.post(
            "/api/v1/user/usernamecheck",
            data={"USERNAME": nickname},
            content_type="application/json",
        )
