from django.db import IntegrityError
from django.test import TransactionTestCase

from user.models import UserModel
from user.tests.services import join_service


class TestCreateUser(TransactionTestCase):
    def setUp(self):
        self.user_tester1 = join_service.create_user(nickname="tester", email="tester@gmail.com")

    # 유저 생성 테스트
    def test_create_user(self) -> None:

        for i in range(1, 4):
            join_service.create_user(nickname=f"tester{i}", email=f"tester{i}@gmail.com")

        # nickname Unique 확인
        with self.assertRaises(IntegrityError):
            join_service.create_user(nickname="tester", email="tester@gmail.com")

        # 유저 숫자 확인
        user_count = UserModel.objects.all()
        self.assertEqual(len(user_count), 4)

    # EMAIL 유효성 검사
    def test_email_modify(self) -> None:
        # EMAIL 유효성 검사 동작 확인 (이미 있는 경우)
        response = join_service.check_to_id_modify(email="tester@gmail.com")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "이미 가입된 이메일입니다.")
        user_check = UserModel.objects.filter(email="tester@gmail.com").exists()
        self.assertEqual(user_check, True)

        # EMAIL 유효성 검사 동작 확인 (특수문자)
        response = join_service.check_to_id_modify(email="tester!@gmail.com")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "이메일은 15자이상, 영문, 숫자만 입력이 가능합니다.")

        # EMAIL 유효성 검사 동작 확인 (길이 제한)
        response = join_service.check_to_id_modify(email="te@gmail.com")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "이메일은 15자이상, 영문, 숫자만 입력이 가능합니다.")

        # EMAIL 유효성 검사 동작 확인 (없는 경우)
        response = join_service.check_to_id_modify(email="tester2@gmail.com")
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response["result"], True)
        with self.assertRaises(UserModel.DoesNotExist):
            UserModel.objects.get(email="tester2@gmail.com")

    # PASSWORD 유효성 검사
    def test_password_modify(self) -> None:
        # PASSWORD 유효성 검사 동작 확인 (조건에 맞지 않는 경우)
        response = join_service.check_to_pw_modify(password="tester2")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "비밀번호는 8자 이상, 영문, 숫자, 특수문자가 포함되어야 합니다.")

        # PASSWORD 유효성 검사 동작 확인 (조건에 맞는 경우)
        response = join_service.check_to_pw_modify(password="tester2@")
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response["result"], True)

    # NICKNAME 유효성 검사
    def test_name_modify(self) -> None:
        # NAME 유효성 검사 동작 확인 (이미 있는 경우)
        response = join_service.check_to_name_modify(nickname="tester")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "이미 가입된 닉네임입니다.")
        user_check = UserModel.objects.filter(username="tester").exists()
        self.assertEqual(user_check, True)

        # NAME 유효성 검사 동작 확인 (특수문자 들어간 경우)
        response = join_service.check_to_name_modify(nickname="tester@")
        self.assertEqual(response.status_code, 422)
        response = response.json()
        self.assertEqual(response["detail"], "닉네임은 5자이상, 영문, 숫자, _ 외에 입력이 불가능합니다.")

        # NICKNAME 유효성 검사 동작 확인 (없는 경우)
        response = join_service.check_to_name_modify(nickname="tester2")
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response["result"], True)
        with self.assertRaises(UserModel.DoesNotExist):
            UserModel.objects.get(username="tester2")
