from django.test import TestCase
from user.tests.services import join_service 
from repositories.tests.services.repo_services import CREATE_REPO_DATA
from bookmark.tests.services.bookmark_service import Create_Bookmark
from bookmark.models import Bookmark

class test_bookmark_api(TestCase):
    def setUp(self) -> None:
        self.user_1 = join_service.create_user("bookmark@naver.com", "bookmark")
        self.repo_1 = CREATE_REPO_DATA(1, "bookmark")
        self.repo_2 = CREATE_REPO_DATA(2, "test")
        self.repo_3 = CREATE_REPO_DATA(3, "django")
        self.bookmark_1 = Create_Bookmark(self.user_1.id, self.repo_1.id)
        self.bookmark_2 = Create_Bookmark(self.user_1.id, self.repo_2.id)
        
        
    # CREATE_BOOKMARK
    def test_create_bookmark_api(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_3.id

        # When
        response = self.client.post(
            f"/api/v1/bookmark/create/",
            data = {
                "USER_ID" : user_id,
                "REPO_ID" : repo_id
            },
            content_type = "application/json"
        )

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()["result"], "success")
        self.assertEqual(response.json()["message"], "Create Success")

    # CREATE_BOOKMARK_FAILED
    def test_create_bookmark_api_failed(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_1.id

        # When
        response_case1 = self.client.post(
            f"/api/v1/bookmark/create/",
            data = {
                "USER_ID" : 999,
                "REPO_ID" : repo_id
            },
            content_type = "application/json"
        )

        response_case2 = self.client.post(
            f"/api/v1/bookmark/create/",
            data = {
                "USER_ID" : user_id,
                "REPO_ID" : 999
            },
            content_type = "application/json"
        )

        # Then
        self.assertEqual(422, response_case1.status_code)
        self.assertEqual(422, response_case2.status_code)
        self.assertEqual(response_case1.json()['result'], 'failed')
        self.assertEqual(response_case2.json()['result'], 'failed')
        self.assertEqual(response_case1.json()['message'], "User is None")
        self.assertEqual(response_case2.json()['message'], "Repository is None")
                

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
        self.assertEqual(response.json()[0]['user_id'], user_id)
        self.assertEqual(response.json()[0]['repo_id'], repo_2_id)
        self.assertEqual(response.json()[1]['repo_id'], repo_1_id)

    # READ_BOOKMARK_FAILED
    def test_read_bookmark_api_failed(self) -> None:
        # Given
        user_2 = join_service.create_user("bookmark2@naver.com", "bookmark2").id

        # When
        response = self.client.get(f"/api/v1/bookmark/read/{user_2}")

        # Then
        self.assertEqual(422, response.status_code)
        self.assertEqual(response.json()['result'], "failed")
        self.assertEqual(response.json()['message'], "Bookmark is None")

    # DELETE_BOOKMARK
    def test_delete_bookmark_api(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_1.id

        # When
        response = self.client.delete(
            f"/api/v1/bookmark/delete",
            data = {
                "USER_ID" : user_id,
                "REPO_ID" : repo_id
            },
            content_type = "application/json"
        )

        read_response = self.client.get(f"/api/v1/bookmark/read/{user_id}")

        # Then
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.json()['result'], 'success')
        self.assertEqual(response.json()['message'], "Delete Success")
        self.assertEqual(len(read_response.json()), 1)
        self.assertEqual(read_response.json()[0]['repo_id'], self.repo_2.id)

    # DELETE_BOOKMARK_FAILED
    def test_delete_bookmark_api_failed(self) -> None:
        # Given
        user_id = self.user_1.id
        repo_id = self.repo_3.id

        # When
        response = self.client.delete(
            f"/api/v1/bookmark/delete",
            data = {
                "USER_ID" : user_id,
                "REPO_ID" : repo_id
            },
            content_type = "application/json"
        )

        # Then
        self.assertEqual(422, response.status_code)
        self.assertEqual(response.json()['result'], "failed")
        self.assertEqual(response.json()['message'], "Bookmark is None")