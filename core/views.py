from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

from .models import Show

class HomeView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'home.html', {'shows': shows})

class ShowDetailView(View):
    def get(self, request, pk):
        show = Show.objects.get(pk=pk)
        return render(request, 'show_detail.html', {'show': show})
    
    def post(self, request, pk):
        quantity = int(request.POST['quantity'])
        show = Show.objects.get(pk=pk)
        cart = request.session.get('cart', [])
        cart.append({'show_id': show.id, 'title': show.title, 'quantity': quantity})
        request.session['cart'] = cart
        return redirect('view_cart')
