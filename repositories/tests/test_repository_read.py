from typing import List

from django.test import TestCase

from repositories.models import Repositories
from repositories.tests.services.repo_services import (create_repo_data,
                                                       read_detail_repo_data,
                                                       read_repo_data)


class Test_read_repository(TestCase):
    def setUp(self):
        create_repo_data(1, "python")
        create_repo_data(2, "test")

    # 데이터 있을 경우 (DETAIL 조회)
    def test_repo_detail_read(self) -> None:
        repo = read_detail_repo_data(1)
        self.assertIsInstance(repo, Repositories)

    # 데이터 없을 경우 (DETAIL 조회)
    def test_repo_detail_read(self) -> None:
        with self.assertRaises(Repositories.DoesNotExist):
            read_detail_repo_data(10)

    # REPOSITORY Keyword 데이터 조회
    def test_repo_read(self) -> None:
        create_repo_data(3, "test")
        create_repo_data(4, "python")
        create_repo_data(5, "django")
        repo_python = read_repo_data("python")
        repo_test = read_repo_data("test")
        repo_django = read_repo_data("django")
        self.assertEqual(len(repo_python), 2)
        self.assertEqual(len(repo_test), 2)
        self.assertEqual(len(repo_django), 1)
