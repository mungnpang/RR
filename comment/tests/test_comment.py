from typing import List

from django.db import IntegrityError
from django.test import TransactionTestCase
from ninja.errors import HttpError

from comment.models import Comment
from comment.tests.services.comment_service import (create_comment,
                                                    delete_comment,
                                                    read_comment,
                                                    update_comment)
from repositories.models import Repositories
from repositories.tests.services.repo_services import create_repo_data
from user.models import UserModel
from user.tests.services.join_service import join_service


class Test_to_comment(TransactionTestCase):
    def setUp(self):
        self.repo1 = create_repo_data(1, "python")
        self.repo2 = create_repo_data(2, "python")
        self.user1 = join_service.create_user("tester1@naver.com", "tester")
        self.user2 = join_service.create_user("tester2@gmail.com", "tester2")
        self.comment = create_comment("testcontent2", self.user1.id, self.repo1.id, None)

    # SUCCEESS_CREATE_COMMENT
    def test_comment_create(self) -> None:
        comment = create_comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.content, "testcontent")
        self.assertEqual(comment.author_id, self.user1.id)
        self.assertIsInstance(comment.author, UserModel)
        self.assertEqual(comment.repo_id, self.repo1.id)
        self.assertIsInstance(comment.repo, Repositories)

    # FAILED_CREATE_COMMENT
    def test_comment_create_failed(self) -> None:
        with self.assertRaises(HttpError):
            create_comment("testcontent", self.user1.id, None, None)
            create_comment("testcontent", None, self.repo1.id, None)
            create_comment(None, self.user1.id, self.repo1.id, None)

    # CREATE_REPLY_COMMENT
    def test_comment_reply_create(self) -> None:
        create_comment("testreply", self.user1.id, self.repo1.id, self.comment.id)
        comments = read_comment(self.repo1.id)
        self.assertEqual(comments[1].content, "testreply")
        self.assertEqual(comments[0].id, comments[1].parent_comment_id)

    # READ_COMMENTS
    def test_comments_read(self) -> List[Comment]:
        create_comment("testcontent", self.user1.id, self.repo1.id, None)
        create_comment("testcontent", self.user1.id, self.repo1.id, None)
        comments = read_comment(self.repo1.id)
        self.assertEqual(len(comments), 3)
        self.assertIsInstance(comments, List)

    # READ_NONE_COMMENTS
    def test_comments_read_none(self) -> None:
        comments_none = read_comment(self.repo2.id)
        self.assertIsInstance(comments_none, list)
        self.assertEqual(len(comments_none), 0)

    # UPDATE_COMMENT
    def test_comment_update(self) -> None:
        comment = create_comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertEqual(comment.content, "testcontent")
        update_comment(comment.id, "update_content")
        updated_comment = read_comment(self.repo1.id)
        self.assertEqual(updated_comment[-1].content, "update_content")

    # UPDATE_COMMENT_FAILED
    def test_comment_update_failed(self) -> None:
        self.assertEqual(self.comment.content, "testcontent2")
        with self.assertRaises(HttpError):
            update_comment(self.comment.id, None)
            update_comment(99, "test")

    # DELETE_COMMENT
    def test_comment_delete(self) -> None:
        comment = create_comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertEqual(len(read_comment(self.repo1.id)), 2)
        delete_comment(comment.id)
        self.assertEqual(len(read_comment(self.repo1.id)), 1)

    # DELETE_COMMENT_FAILED
    def test_comment_delete_failed(self) -> None:
        with self.assertRaises(Comment.DoesNotExist):
            delete_comment(2)
