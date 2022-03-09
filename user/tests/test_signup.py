from django.test import TestCase
from user.models import UserModel
from django.db import IntegrityError, transaction

class TestCreateUser(TestCase):
    def test_create_user(self) -> None:
        # 유저 생성
        UserModel.objects.create(username="tester")
        UserModel.objects.create(username="tester2")
        UserModel.objects.create(username="tester3")
        
        # username Unique 확인
        with self.assertRaises(IntegrityError):
            check_unique("tester2")

        # 유저 숫자 확인
        user_count = UserModel.objects.all()
        self.assertEqual(len(user_count), 3)

@transaction.atomic
def check_unique(username: str) -> UserModel:
    users = UserModel.objects.create(username=username)
    return users

