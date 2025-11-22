from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# SIGNUP
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', '')
        password1 = request.POST['password']
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, email=email, password=password1)
        return redirect('login')

    return render(request, 'signup.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')  # go to main homepage
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')
