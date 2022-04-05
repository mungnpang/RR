from django.db.utils import IntegrityError
from django.test import TestCase

from bookmark.models import Bookmark
from bookmark.tests.services.bookmark_service import Create_Bookmark, Delete_BookMark, Read_Bookmark
from repositories.tests.services import CREATE_REPO_DATA
from user.tests.services import join_service


class Test_bookmark(TestCase):
    def setUp(self) -> None:
        self.user_1 = join_service.create_user("tester1@naver.com", "tester1")
        self.user_2 = join_service.create_user("tester2@naver.com", "tester2")
        self.repo_1 = CREATE_REPO_DATA(1, "python")
        self.repo_2 = CREATE_REPO_DATA(2, "python")
        self.bookmark_1 = Create_Bookmark(self.user_1.id, self.repo_1.id)
        self.bookmark_2 = Create_Bookmark(self.user_2.id, self.repo_2.id)

    # CREATE_BOOKMARK
    def test_create_bookmark(self) -> str:
        create = Create_Bookmark(self.user_1.id, self.repo_2.id)
        self.assertIsInstance(create, Bookmark)

    # CREATE_BOOKMARK_UNIQUE_VALID
    def test_create_bookmark_unique(self) -> str:
        create = Create_Bookmark(self.user_1.id, self.repo_2.id)
        self.assertIsInstance(create, Bookmark)
        with self.assertRaises(IntegrityError):
            Create_Bookmark(self.user_1.id, self.repo_1.id)

    # CREATE_BOOKMARK_FAILED
    def test_create_bookmark_failed(self) -> str:
        create = Create_Bookmark(self.user_1.id, 5)
        self.assertEqual(create, "Repository is None")
        create = Create_Bookmark(5, self.repo_1.id)
        self.assertEqual(create, "User is None")

    # READ_BOOKMARK
    def test_read_bookmark(self) -> str:
        Create_Bookmark(self.user_1.id, self.repo_2.id)
        read = Read_Bookmark(self.user_1.id)
        self.assertIsInstance(read, list)
        self.assertEqual(len(read), 2)
        self.assertEqual(read[0].repo_id, self.repo_1.id)
        self.assertEqual(read[1].repo_id, self.repo_2.id)

    # READ_BOOKMARK IS NONE
    def test_read_bookmark(self) -> str:
        user_3 = join_service.create_user("tester3@naver.com", "tester3")
        read = Read_Bookmark(user_3.id)
        self.assertEqual(len(read), 0)
        self.assertEqual(read, [])
        read = Read_Bookmark(4)
        self.assertEqual(read, "User is None")

    # DELETE_BOOKMARK
    def test_delete_bookmark(self) -> str:
        read = Read_Bookmark(self.user_1.id)
        self.assertEqual(len(read), 1)
        Delete_BookMark(self.user_1.id, self.repo_1.id)
        read = Read_Bookmark(self.user_1.id)
        self.assertEqual(len(read), 0)

    # DELETE_BOOKMARK FAILED
    def test_delete_bookmark_failed(self) -> str:
        delete = Delete_BookMark(99, self.repo_1.id)
        self.assertEqual(delete, "User is None")
        delete = Delete_BookMark(self.user_1.id, 99)
        self.assertEqual(delete, "Repository is None")
        delete = Delete_BookMark(self.user_2.id, self.repo_1.id)
        self.assertEqual(delete, "Bookmark is None")
