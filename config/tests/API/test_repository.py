from django.test import TestCase

from repositories.tests.services.repo_services import create_repo_data


class test_repository_api(TestCase):
    def setUp(self) -> None:
        self.repo_1 = create_repo_data(1, "test")
        self.repo_2 = create_repo_data(2, "test")
        self.repo_3 = create_repo_data(3, "django")

    # READ_REPO
    def test_read_api(self) -> None:
        # Given
        keyword = "test"
        second_keyword = "django"

        # When
        response_1 = self.client.get(f"/api/v1/repository/{keyword}/0")
        response_2 = self.client.get(f"/api/v1/repository/{second_keyword}/0")

        # Then
        self.assertEqual(200, response_1.status_code)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(keyword, response_1.json()[0]["keyword"])
        self.assertEqual(second_keyword, response_2.json()[0]["keyword"])

    # READ_REPO FAILED
    def test_read_api_failed(self) -> None:
        # Given
        keyword = " "

        # When
        response = self.client.get(f"/api/v1/repository/{keyword}/0")

        # Then
        self.assertEqual(404, response.status_code)
        response = response.json()
        self.assertEqual(response["detail"], "Keyword Not Found")

    # READ_DETAIL_REPO
    def test_detail_read_api(self) -> None:
        # Given
        repo_id = self.repo_1.id

        # When
        response = self.client.get(f"/api/v1/repository/detail/{repo_id}")

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(repo_id, response.json()["id"])

    # READ_DETAIL_REPO_FAILED
    def test_detail_read_api_failed(self) -> None:
        # Given
        repo_id = 9999

        # When
        response = self.client.get(f"/api/v1/repository/detail/{repo_id}")

        # Then
        self.assertEqual(404, response.status_code)
        response = response.json()
        self.assertEqual(response["detail"], "Repository Not Found.")
