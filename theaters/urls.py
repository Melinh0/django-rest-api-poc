from django.urls import path
from .views import TheatersList, TheaterDetailAPIView

urlpatterns = [
    path("", TheatersList.as_view()),
    path("<int:number>/", TheaterDetailAPIView.as_view()),
]
