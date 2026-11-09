from djongo import models
from movies.models import Movie
from theaters.models import Theater


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie")
    theater = models.ForeignKey(
        Theater, on_delete=models.CASCADE, verbose_name="Theater"
    )
    start_time = models.DateTimeField("Start Time")

    def __str__(self):
        return f"{self.movie} at {self.theater} - {self.start_time}"
