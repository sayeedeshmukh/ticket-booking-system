from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from datetime import date


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # or wherever you want to redirect after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

from .models import Show, Booking

class HomeView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'home.html', {'shows': shows})



from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
class ViewAllBookings(View):
    def get(self, request):
        bookings = Booking.objects.select_related('user', 'show').all()
        return render(request, 'core/all_bookings.html', {'bookings': bookings})

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Show, Booking
from django.shortcuts import render, redirect

@method_decorator(login_required, name='dispatch')
class AddShowView(View):
    def get(self, request):
        return render(request, 'core/add_show.html')
    
    def post(self, request):
        title = request.POST['title']
        date = request.POST['date']
        time = request.POST['time']
        seats = request.POST['seats']
        Show.objects.create(title=title, date=date, time=time, seats=seats)
        return redirect('home') 
    
@method_decorator(login_required, name='dispatch')
class DeleteShowView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request,'core/delete_show.html', {'show': show})
    
    def post(self, request, pk):
        show = Show.objects.get(pk=pk)
        show.delete()
        return redirect('home')

@method_decorator(login_required, name='dispatch')
class ViewAllBookings(View):
    def get(self, request):
        bookings = Booking.objects.select_related('user', 'show').all()
        return render(request, 'core/all_bookings.html', {'bookings': bookings})
    
class ShowListView(View):
    def get(self, request):
        if Show.objects.count() == 0:
     
            Show.objects.create(
                title="Hamlet",
                description="A Shakespearean tragedy about revenge and madness.",
                date=date(2025, 5, 10),
                time="19:00",
                venue="City Theater",
                seats=100,  
                price=25.00 
                )
            Show.objects.create(
                title="The Phantom of the Opera",
                description="A mysterious tale of love and music beneath an opera house.",
                date=date(2025, 5, 15),
                time="18:30",
                venue="Grand Opera Hall",
                seats=150,  
                price=30.00  
            )
            
        shows = Show.objects.all()
        return render(request, 'show-list.html', {'shows': shows})

@method_decorator(login_required, name='dispatch')
class BookShowView(View):
    def get(self, request, show_id):
        show = Show.objects.get(id=show_id)
        return render(request, 'book_show.html', {'show': show})
    
    def post(self, request, show_id):
        quantity = int(request.POST['quantity'])
        show = Show.objects.get(id=show_id)
        

        if quantity > show.seats:
            return render(request, 'book_show.html', {
                'show': show,
                'error': 'Not enough seats available'
            })
        

        Booking.objects.create(
            user=request.user,
            show=show,
            quantity=quantity
        )
        

        show.seats -= quantity
        show.save()
        
        return redirect('booking-confirmation')  
    
@method_decorator(login_required, name='dispatch')
class BookingConfirmationView(View):
    def get(self, request):
        return render(request, 'booking_confirmation.html')