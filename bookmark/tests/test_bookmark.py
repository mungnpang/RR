from django.db.utils import IntegrityError
from django.test import TestCase
from ninja.errors import HttpError

from bookmark.models import Bookmark
from bookmark.tests.services.bookmark_service import (create_bookmark,
                                                      delete_bookmark,
                                                      read_bookmark)
from repositories.tests.services import create_repo_data
from user.tests.services import join_service


class Test_bookmark(TestCase):
    def setUp(self) -> None:
        self.user_1 = join_service.create_user("tester1@naver.com", "tester1")
        self.user_2 = join_service.create_user("tester2@naver.com", "tester2")
        self.repo_1 = create_repo_data(1, "python")
        self.repo_2 = create_repo_data(2, "python")
        self.bookmark_1 = create_bookmark(self.user_1.id, self.repo_1.id)
        self.bookmark_2 = create_bookmark(self.user_2.id, self.repo_2.id)

    # CREATE_BOOKMARK
    def test_create_bookmark(self) -> str:
        create_bookmark(self.user_1.id, self.repo_2.id)

    # CREATE_BOOKMARK_UNIQUE_VALID
    def test_create_bookmark_unique(self) -> str:
        create_bookmark(self.user_1.id, self.repo_2.id)
        with self.assertRaises(IntegrityError):
            create_bookmark(self.user_1.id, self.repo_1.id)

    # CREATE_BOOKMARK_FAILED
    def test_create_bookmark_failed(self) -> str:
        with self.assertRaises(HttpError):
            create = create_bookmark(self.user_1.id, 5)
            self.assertEqual(create.status_code, 404)
            self.assertEqual(create["detail"], "User Not Found")
            create = create_bookmark(5, self.repo_1.id)
            self.assertEqual(create.status_code, 404)
            self.assertEqual(create["detail"], "Repository Not Found")

    # READ_BOOKMARK
    def test_read_bookmark(self) -> str:
        create_bookmark(self.user_1.id, self.repo_2.id)
        read = read_bookmark(self.user_1.id)
        self.assertIsInstance(read, list)
        self.assertEqual(len(read), 2)
        self.assertEqual(read[0].repo_id, self.repo_1.id)
        self.assertEqual(read[1].repo_id, self.repo_2.id)

    # READ_BOOKMARK IS NONE
    def test_read_bookmark(self) -> str:
        user_3 = join_service.create_user("tester3@naver.com", "tester3")
        read = read_bookmark(user_3.id)
        self.assertEqual(len(read), 0)
        self.assertEqual(read, [])
        with self.assertRaises(HttpError):
            read = read_bookmark(4)
            self.assertEqual(read.status_code, 404)
            self.assertEqual(read["detail"], "User Not Found")

    # DELETE_BOOKMARK
    def test_delete_bookmark(self) -> str:
        read = read_bookmark(self.user_1.id)
        self.assertEqual(len(read), 1)
        delete_bookmark(self.user_1.id, self.repo_1.id)
        read = read_bookmark(self.user_1.id)
        self.assertEqual(len(read), 0)

    # DELETE_BOOKMARK FAILED
    def test_delete_bookmark_failed(self) -> str:
        with self.assertRaises(HttpError):
            delete = delete_bookmark(99, self.repo_1.id)
            self.assertEqual(delete.status_code, 404)
            self.assertEqual(delete["detail"], "User Not Found")
            delete = delete_bookmark(self.user_1.id, 99)
            self.assertEqual(delete.status_code, 404)
            self.assertEqual(delete["detail"], "Repository Not Found")
            delete = delete_bookmark(self.user_2.id, self.repo_1.id)
            self.assertEqual(delete.status_code, 404)
            self.assertEqual(delete["detail"], "Bookmark Not Found")
