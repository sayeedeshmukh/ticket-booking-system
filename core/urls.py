from django.urls import path
from .views import RegisterView, LoginView, LogoutView,HomeView,ShowDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('show/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),


]
