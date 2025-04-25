from django.urls import path
from .views import RegisterView, LoginView, LogoutView, HomeView, AddShowView, ViewAllBookings,EditShowView,DeleteShowView,ShowListView,BookShowView,BookingConfirmationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('admin/add-show/', AddShowView.as_view(), name='add_show'),
    path('admin/edit-show/<int:pk>/', EditShowView.as_view(), name='edit_show'),
    path('admin/bookings/', ViewAllBookings.as_view(), name='view_bookings'),
    path('admin/delete-show/<int:pk>/', DeleteShowView.as_view(), name='delete_show'),
    path('shows/', ShowListView.as_view(), name='show-list'),
    path('book/<int:show_id>/', BookShowView.as_view(), name='book-show'),
    path('booking-confirmation/', BookingConfirmationView.as_view(), name='booking-confirmation'),
]   
