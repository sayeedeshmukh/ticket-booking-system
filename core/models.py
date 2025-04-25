from django.db import models
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect


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

@method_decorator(login_required, name='dispatch')
class EditShowView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'core/edit_show.html', {'show': show})
    
    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.title = request.POST['title']
        show.date = request.POST['date']
        show.time = request.POST['time']
        show.seats = request.POST['seats']
        show.save()
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeleteShowView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'adminpanel/delete_show.html', {'show': show})
    
    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.delete()
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class ViewAllBookings(View):
    def get(self, request):
        bookings = Booking.objects.select_related('user', 'show').all()
        return render(request, 'adminpanel/all_bookings.html', {'bookings': bookings})
