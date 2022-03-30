from typing import List
from django.test import TestCase
from user.tests.services.join_service import join_service
from comment.tests.services.comment_service import Create_Comment, Read_Comment, Update_Comment, Delete_Comment
from comment.models import Comment
from repositories.tests.services.repo_services import CREATE_REPO_DATA
from user.models import UserModel
from repositories.models import Repositories


class Test_to_comment(TestCase):
    def setUp(self):
        self.repo1 = CREATE_REPO_DATA(1, "python")
        self.repo2 = CREATE_REPO_DATA(2, "python")
        self.user1= join_service.create_user("tester1@naver.com", "tester")
        self.user2= join_service.create_user("tester2@gmail.com", "tester2")
        self.comment = Create_Comment("testcontent2", self.user1.id, self.repo1.id , None)

    # SUCCEESS_CREATE_COMMENT
    def test_comment_create(self) -> None:
        comment = Create_Comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.content, "testcontent")
        self.assertEqual(comment.author_id, self.user1.id)
        self.assertIsInstance(comment.author,UserModel)
        self.assertEqual(comment.repo_id,self.repo1.id)
        self.assertIsInstance(comment.repo, Repositories)
    
    # FAILED_CREATE_COMMENT
    def test_comment_create_failed(self) -> None:
        comment = Create_Comment("testcontent", self.user1.id, None, None)
        self.assertEqual(comment, "Empty Space")
        comment2 = Create_Comment("testcontent", None, self.repo1.id, None)
        self.assertEqual(comment2, "Empty Space")
        comment3 = Create_Comment(None, self.user1.id, self.repo1.id, None)
        self.assertEqual(comment3, "Empty Space")

    # CREATE_REPLY_COMMENT
    def test_comment_reply_create(self) -> None:
        Create_Comment("testreply", self.user1.id, self.repo1.id, self.comment.id)
        comments = Read_Comment(self.repo1.id)
        self.assertEqual(comments[1].content, "testreply")
        self.assertEqual(comments[0].id, comments[1].parent_comment_id)

    # READ_COMMENTS
    def test_comments_read(self)-> List[Comment]:
        Create_Comment("testcontent", self.user1.id, self.repo1.id, None)
        Create_Comment("testcontent", self.user1.id, self.repo1.id, None)
        comments = Read_Comment(self.repo1.id)
        self.assertEqual(len(comments), 3)
        self.assertIsInstance(comments, List)
    
    # READ_NONE_COMMENTS
    def test_comments_read_none(self)-> str:
        comments_none = Read_Comment(self.repo2.id)
        self.assertIsInstance(comments_none, str)
        self.assertEqual(comments_none, "Data is None")

    # UPDATE_COMMENT
    def test_comment_update(self) -> str:
        comment = Create_Comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertEqual(comment.content, "testcontent")
        comment_update = Update_Comment(comment.id, "update_content")
        self.assertIsInstance(comment_update, Comment)
        self.assertEqual(comment_update.content, "update_content")

    # UPDATE_COMMENT_FAILED
    def test_comment_update_failed(self) -> str:
        self.assertEqual(self.comment.content, "testcontent2")
        comment_update = Update_Comment(self.comment.id, None)
        self.assertEqual(comment_update, "Comment is Empty")
        comment_update = Update_Comment(99, "test")
        self.assertEqual(comment_update, "Comment is None")

    # DELETE_COMMENT
    def test_comment_delete(self) -> str:
        comment = Create_Comment("testcontent", self.user1.id, self.repo1.id, None)
        self.assertEqual(len(Read_Comment(self.repo1.id)), 2)
        comment_delete = Delete_Comment(comment.id)
        self.assertEqual(comment_delete, "Delete Success")
        self.assertEqual(len(Read_Comment(self.repo1.id)), 1)
    
    # DELETE_COMMENT_FAILED
    def test_comment_delete_failed(self) -> str:
        comment_delete = Delete_Comment(2)
        self.assertEqual(comment_delete, "Comment is None")