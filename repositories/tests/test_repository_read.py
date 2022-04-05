from typing import List

from django.test import TestCase

from repositories.models import Repositories
from repositories.tests.services.repo_services import (CREATE_REPO_DATA,
                                                       READ_DETAIL_REPO_DATA,
                                                       READ_REPO_DATA)


class Test_read_repository(TestCase):
    def setUp(self):
        CREATE_REPO_DATA(1, "python")
        CREATE_REPO_DATA(2, "test")

    # 데이터 있을 경우 (DETAIL 조회)
    def test_repo_detail_read(self) -> Repositories:
        repo = READ_DETAIL_REPO_DATA(1)
        self.assertIsInstance(repo, Repositories)

    # 데이터 없을 경우 (DETAIL 조회)
    def test_repo_detail_read(self) -> Repositories:
        repo = READ_DETAIL_REPO_DATA(10)
        self.assertEqual(repo, "Data is None")

    # REPOSITORY Keyword 데이터 조회
    def test_repo_read(self) -> List[Repositories]:
        CREATE_REPO_DATA(3, "test")
        CREATE_REPO_DATA(4, "python")
        CREATE_REPO_DATA(5, "django")
        repo_python = READ_REPO_DATA("python")
        repo_test = READ_REPO_DATA("test")
        repo_django = READ_REPO_DATA("django")
        self.assertEqual(len(repo_python), 2)
        self.assertEqual(len(repo_test), 2)
        self.assertEqual(len(repo_django), 1)
