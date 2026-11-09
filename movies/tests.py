from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie


class MovieAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie_data = {
            "name": "Inception",
            "director": "Christopher Nolan",
            "duration": 148,
        }

    def test_create_movie(self):
        response = self.client.post("/api/movies/", self.movie_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_movies(self):
        Movie.objects.create(**self.movie_data)
        response = self.client.get("/api/movies/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_movie(self):
        movie = Movie.objects.create(**self.movie_data)
        response = self.client.get(f"/api/movies/{movie.name}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_movie(self):
        movie = Movie.objects.create(**self.movie_data)
        updated = {
            "name": "Inception",
            "director": "Christopher Nolan",
            "duration": 150,
        }
        response = self.client.put(
            f"/api/movies/{movie.name}/", updated, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_movie(self):
        movie = Movie.objects.create(**self.movie_data)
        response = self.client.delete(f"/api/movies/{movie.name}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
