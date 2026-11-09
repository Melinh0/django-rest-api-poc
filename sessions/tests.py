from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from movies.models import Movie
from theaters.models import Theater
from .models import Session


class SessionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(
            name="Inception",
            director="Christopher Nolan",
            duration=148,
        )
        self.theater = Theater.objects.create(
            number=1,
            description="Main theater",
        )
        self.session_data = {
            "movie": self.movie.id,
            "theater": self.theater.id,
            "start_time": "2024-01-15T20:00:00Z",
        }

    def test_create_session(self):
        response = self.client.post(
            "/api/sessions/", self.session_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_sessions(self):
        Session.objects.create(
            movie=self.movie,
            theater=self.theater,
            start_time="2024-01-15T20:00:00Z",
        )
        response = self.client.get("/api/sessions/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_session(self):
        session = Session.objects.create(
            movie=self.movie,
            theater=self.theater,
            start_time="2024-01-15T20:00:00Z",
        )
        response = self.client.get(f"/api/sessions/{session.id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_session(self):
        session = Session.objects.create(
            movie=self.movie,
            theater=self.theater,
            start_time="2024-01-15T20:00:00Z",
        )
        updated = {
            "movie": self.movie.id,
            "theater": self.theater.id,
            "start_time": "2024-01-16T20:00:00Z",
        }
        response = self.client.put(
            f"/api/sessions/{session.id}/", updated, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_session(self):
        session = Session.objects.create(
            movie=self.movie,
            theater=self.theater,
            start_time="2024-01-15T20:00:00Z",
        )
        response = self.client.delete(f"/api/sessions/{session.id}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
