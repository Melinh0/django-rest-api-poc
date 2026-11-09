from djongo import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name
