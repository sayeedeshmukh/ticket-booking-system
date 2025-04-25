from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    seats = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
