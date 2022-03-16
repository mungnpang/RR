from django.test import TestCase
from repositories.tests.services.repo_services import CREATE_REPO_DATA

class test_repository_api(TestCase):
    def setUp(self) -> None:
        self.repo_1 = CREATE_REPO_DATA(1, "test")
        self.repo_2 = CREATE_REPO_DATA(2, "test")
        self.repo_3 = CREATE_REPO_DATA(3, "django")

    # READ_REPO
    def test_read_api(self) -> None:
        # Given
        keyword = "test"
        second_keyword = "django"

        # When
        response_1 = self.client.get(f"/api/v1/repository/{keyword}")
        response_2 = self.client.get(f"/api/v1/repository/{second_keyword}")

        # Then
        self.assertEqual(200, response_1.status_code)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(keyword, response_1.json()[0]['keyword'])
        self.assertEqual(second_keyword, response_2.json()[0]['keyword'])

    # READ_REPO FAILED
    def test_read_api_failed(self) -> None:
        # Given
        keyword = "failed"

        # When
        response = self.client.get(f"/api/v1/repository/{keyword}")

        # Then
        self.assertEqual(422, response.status_code)
        self.assertEqual(response.json()['message'], "Keyword is Empty")

    # READ_DETAIL_REPO
    def test_detail_read_api(self) -> None:
        # Given
        repo_id = 1

        # When
        response = self.client.get(f"/api/v1/repository/detail/{repo_id}")

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(repo_id, response.json()['repo_id'])

    # READ_DETAIL_REPO_FAILED
    def test_detail_read_api_failed(self) -> None:
        # Given
        repo_id = 9999

        # When
        response = self.client.get(f"/api/v1/repository/detail/{repo_id}")

        # Then
        self.assertEqual(422, response.status_code)
        self.assertEqual(response.json()['message'], "Repository is None")



