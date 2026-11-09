from djongo import models


class Theater(models.Model):
    number = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return f"Theater {self.number}"
