from django.test import Client, TestCase

from comment.tests.services.comment_service import create_comment
from repositories.tests.services.repo_services import create_repo_data
from user.tests.services.join_service import join_service


class test_comment_api(TestCase):
    def setUp(self) -> None:
        self.repo_1 = create_repo_data(1, "test")
        self.user_1 = join_service.create_user("tester2@naver.com", "tester")
        self.comment = create_comment("test content", self.user_1.id, self.repo_1.id, None)
        self.reply_comment = create_comment("test reply content", self.user_1.id, self.repo_1.id, self.comment.id)
        self.client = Client()
        self.client.force_login(self.user_1)

    # CREATE_COMMENT
    def test_create_comment_api(self) -> None:
        # Given
        repo_id = self.repo_1.id
        content = "comment_test"

        # When
        response = self.client.post(
            f"/api/v1/comment/create/",
            data={"REPO_ID": repo_id, "CONTENT": content},
            content_type="application/json",
        )

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")

    # CREATE_COMMENT_FAILED
    def test_create_comment_api_failed(self) -> None:
        # Given
        repo_id = 999
        content = "failed_test"

        # When
        response = self.client.post(
            f"/api/v1/comment/create/",
            data={"REPO_ID": repo_id, "CONTENT": content},
            content_type="application/json",
        )

        # Then
        self.assertEqual(422, response.status_code)
        self.assertEqual(response.json()["detail"], "Empty Space")

    # READ_COMMENT
    def test_read_comment_api(self) -> None:
        # Given
        repo_id = self.repo_1.id

        # When
        response = self.client.get(f"/api/v1/comment/read/{repo_id}")

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(repo_id, response.json()[0]["repo_id"])

    # READ_COMMENT_FAILED
    def test_read_comment_api_failed(self) -> None:
        # Given
        repo_id = 999

        # When
        response = self.client.get(f"/api/v1/comment/read/{repo_id}")

        # Then
        self.assertEqual(404, response.status_code)
        self.assertEqual(response.json()["detail"], "Comment is None")

    # UPDATE_COMMENT
    def test_update_comment_api(self) -> None:
        # Given
        comment_id = self.comment.id
        content = "update"

        # When
        response = self.client.put(
            f"/api/v1/comment/update",
            data={"COMMENT_ID": comment_id, "CONTENT": content},
            content_type="application/json",
        )
        update_comment = self.client.get(f"/api/v1/comment/read/{self.repo_1.id}")

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")
        self.assertEqual(update_comment.json()[0]["content"], "update")

    # UPDATE_COMMENT_FAILED
    def test_update_comment_api_failed(self) -> None:
        # Given
        comment_id = self.comment.id
        content = ""

        # When
        response_case1 = self.client.put(
            f"/api/v1/comment/update",
            data={"COMMENT_ID": comment_id, "CONTENT": content},
            content_type="application/json",
        )

        response_case2 = self.client.put(
            f"/api/v1/comment/update",
            data={"COMMENT_ID": 999, "CONTENT": "update_failed"},
            content_type="application/json",
        )

        # Then
        self.assertEqual(422, response_case1.status_code)
        self.assertEqual(404, response_case2.status_code)
        self.assertEqual(response_case1.json()["detail"][0]["msg"], "Empty Space")
        self.assertEqual(response_case2.json()["detail"], "Comment is None")

    # DELETE_COMMENT
    def test_delete_comment_api(self) -> None:
        # Given
        comment_id = self.comment.id

        # When
        response = self.client.delete(
            f"/api/v1/comment/delete",
            data={"COMMENT_ID": comment_id},
            content_type="application/json",
        )

        delete_comment = self.client.get(f"/api/v1/comment/read/{self.repo_1.id}")

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")
        self.assertEqual(404, delete_comment.status_code)
        self.assertEqual(delete_comment.json()["detail"], "Comment is None")

    # DELETE_COMMENT_FAILED
    def test_delete_comment_api_failed(self) -> None:
        # Given
        comment_id = 999

        # When
        response = self.client.delete(
            f"/api/v1/comment/delete",
            data={"COMMENT_ID": comment_id},
            content_type="application/json",
        )

        # Then
        self.assertEqual(404, response.status_code)
        self.assertEqual(response.json()["detail"], "Comment is None")
