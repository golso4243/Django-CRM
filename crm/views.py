from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # Login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate User
        user = authenticate(request, username=username, password=password)
        # If user is not None, login user
        if user is not None:
            login(request, user)
            # Send a success message
            messages.success(request, 'Login successful')
            # Redirect to home page
            return redirect('home')
        else:
            # Send an error message
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        # If request is not POST, render the home page
        return render(request, 'home.html', {})

# TODO Implement login_user function (seperate from homepage)
# def login_user(request):
#     pass

# Logout


def logout_user(request):
    logout(request)
    # Send a success message
    messages.success(request, 'Logged out successfully')
    # Redirect to home page
    return redirect('home')
