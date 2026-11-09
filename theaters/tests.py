from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Theater


class TheaterAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.theater_data = {
            "number": 1,
            "description": "Main theater",
        }

    def test_create_theater(self):
        response = self.client.post("/api/theaters/", self.theater_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_theaters(self):
        Theater.objects.create(**self.theater_data)
        response = self.client.get("/api/theaters/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_theater(self):
        theater = Theater.objects.create(**self.theater_data)
        response = self.client.get(
            f"/api/theaters/{theater.number}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_theater(self):
        theater = Theater.objects.create(**self.theater_data)
        updated = {"number": 1, "description": "Updated theater"}
        response = self.client.put(
            f"/api/theaters/{theater.number}/", updated, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_theater(self):
        theater = Theater.objects.create(**self.theater_data)
        response = self.client.delete(
            f"/api/theaters/{theater.number}/", format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
