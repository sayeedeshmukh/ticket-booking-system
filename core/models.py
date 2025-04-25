from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    seats = models.PositiveIntegerField()

    def __str__(self):
        return self.title
