from django.db.utils import IntegrityError
from django.test import Client, TransactionTestCase

from bookmark.models import Bookmark
from bookmark.tests.services.bookmark_service import create_bookmark
from repositories.tests.services.repo_services import create_repo_data
from user.tests.services import join_service


class test_bookmark_api(TransactionTestCase):
    def setUp(self) -> None:
        self.user_1 = join_service.create_user("bookmark@naver.com", "bookmark")
        self.repo_1 = create_repo_data(1, "bookmark")
        self.repo_2 = create_repo_data(2, "test")
        self.repo_3 = create_repo_data(3, "django")
        self.bookmark_1 = create_bookmark(self.user_1.id, self.repo_1.id)
        self.bookmark_2 = create_bookmark(self.user_1.id, self.repo_2.id)
        self.client = Client()
        self.client.force_login(self.user_1)

    # CREATE_BOOKMARK
    def test_create_bookmark_api(self) -> None:
        # Given
        repo_id = self.repo_3.id

        # When
        response = self.client.post(
            f"/api/v1/bookmark/create/",
            data={"REPO_ID": repo_id},
            content_type="application/json",
        )

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")

        # Then DB check
        db_check = Bookmark.objects.get(user_id=self.user_1.id, repo_id=repo_id)
        self.assertEqual(repo_id, db_check.repo.id)

    # CREATE_BOOKMARK_FAILED
    def test_create_bookmark_api_failed(self) -> None:
        # Given
        repo_id = self.repo_1.id

        # When & Then
        with self.assertRaises(IntegrityError):
            self.client.post(
                f"/api/v1/bookmark/create/",
                data={"REPO_ID": repo_id},
                content_type="application/json",
            )

        # When
        response_case2 = self.client.post(
            f"/api/v1/bookmark/create/",
            data={"REPO_ID": 999},
            content_type="application/json",
        )

        # Then

        self.assertEqual(404, response_case2.status_code)
        self.assertEqual(response_case2.json()["detail"], "User or Repository is None")

    # READ_BOOKMARK
    def test_read_bookmark_api(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_1_id = self.repo_1.id
        repo_2_id = self.repo_2.id

        # When
        response = self.client.get(f"/api/v1/bookmark/read/{user_id}")

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["repo"]["id"], repo_2_id)
        self.assertEqual(response.json()[1]["repo"]["id"], repo_1_id)

    # READ_BOOKMARK_FAILED
    def test_read_bookmark_api_failed(self) -> None:
        # Given
        user_2 = join_service.create_user("bookmark2@naver.com", "bookmark2").id

        # When
        response = self.client.get(f"/api/v1/bookmark/read/{user_2}")

        # Then
        self.assertEqual(404, response.status_code)
        self.assertEqual(response.json()["detail"], "Bookmark is None")

    # DELETE_BOOKMARK
    def test_delete_bookmark_api(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_1.id

        # When
        response = self.client.delete(
            f"/api/v1/bookmark/delete",
            data={"USER_ID": user_id, "REPO_ID": repo_id},
            content_type="application/json",
        )

        read_response = self.client.get(f"/api/v1/bookmark/read/{user_id}")

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")
        self.assertEqual(len(read_response.json()), 1)
        self.assertEqual(read_response.json()[0]["repo"]["id"], self.repo_2.id)

    # DELETE_BOOKMARK_FAILED
    def test_delete_bookmark_api_failed(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_3.id

        # When
        response = self.client.delete(
            f"/api/v1/bookmark/delete",
            data={"USER_ID": user_id, "REPO_ID": repo_id},
            content_type="application/json",
        )

        # Then
        self.assertEqual(404, response.status_code)
        self.assertEqual(response.json()["detail"], "Bookmark is None")
