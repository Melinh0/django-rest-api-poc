from django.urls import path
from .views import MoviesList, MovieDetailAPIView

urlpatterns = [
    path("", MoviesList.as_view()),
    path("<str:name>/", MovieDetailAPIView.as_view()),
]
