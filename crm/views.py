# Importing necessary functions for rendering templates and redirecting views
from django.shortcuts import render, redirect
# Importing necessary functions for authenticating, logging in and logging out users
from django.contrib.auth import authenticate, login, logout
# Importing messages module for sending messages to the user interface (UI)
from django.contrib import messages
# Importing the SignUpForm and AddRecordForm from forms.py for user registration
from .forms import SignUpForm, AddRecordForm
# Importing the Record model from models.py for database operations (CRUD)
from .models import Record

# Home view - renders the homepage or redirects to login if user is not authenticated


def home(request):

    # Retrieves all records from the database
    records = Record.objects.all()

    # Login User if request is POST
    if request.method == 'POST':

        # Get username and password from POST request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate User
        user = authenticate(request, username=username, password=password)

        # If user is not None (valid credentials)
        if user is not None:

            # Log in the user
            login(request, user)

            # Send a success message
            messages.success(request, 'Login successful')

            # Redirect to home page
            return redirect('home')

        # If user is None (invalid credentials)
        else:

            # Send an error message
            messages.error(request, 'Invalid username or password')

            # Redirect to home page
            return redirect('home')

    # If request is POST
    else:

        # Render the home page with the records
        return render(request, 'home.html', {'records': records})

# TODO Implement login_user function (seperate from homepage)
# def login_user(request):
#     pass


# Logout View - Logs out the user and redirects to the home page


def logout_user(request):

    # Log out the user
    logout(request)

    # Send a success message
    messages.success(request, 'Logged out successfully')

    # Redirect to home page
    return redirect('home')


# Register View - Registers a new user and logs them in


def register_user(request):

    # If request is POST
    if request.method == 'POST':

        # Create a new SignUpForm instance with the POST data
        form = SignUpForm(request.POST)

        # If form is valid
        if form.is_valid():

            # Save the form
            form.save()

            # Get username and password from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            # Log in the user
            login(request, user)

            # Send a success message
            messages.success(request, 'Account created successfully')

            # Redirect to home page
            return redirect('home')

    # If not POST request
    else:

        # Create a new instance of the SignUpForm
        form = SignUpForm()

        # Render the register page with the form
        return render(request, 'register.html', {'form': form})

    # Render the register page with the form if form is invalid
    return render(request, 'register.html', {'form': form})


# Customer Record View - Renders the customer record page

def customer_record(request, pk):
    # If user is authenticated
    if request.user.is_authenticated:

        # Get the record with the id from the database
        customer_record = Record.objects.get(id=pk)

        # Render the record page with the record
        return render(request, 'record.html', {'customer_record': customer_record})

    # If user is not authenticated
    else:

        # Send an error message
        messages.error(request, 'Please Login to View Customer Records')

        # Redirect to home page
        return redirect('home')


# Delete Record

def delete_record(request, pk):
    # If user is authenticated
    if request.user.is_authenticated:

        # Get the record with the id from the database
        record = Record.objects.get(id=pk)

        # Delete the record
        record.delete()

        # Send a success message
        messages.success(request, 'Record Deleted Successfully')

        # Redirect to home page
        return redirect('home')

    # If user is not authenticated
    else:

        # Send an error message
        messages.error(request, 'Please Login to Delete Customer Records')

        # Redirect to home page
        return redirect('home')


# Add Record View - Adds a new record to the database


def add_record(request):

    # Create a new instance of the AddRecordForm
    form = AddRecordForm(request.POST or None)

    # If user is authenticated
    if request.user.is_authenticated:

        # If request is POST
        if request.method == 'POST':

            # If form is valid
            if form.is_valid():

                # Save the form
                record = form.save()

                # Success Message for Record Added
                messages.success(request, 'Record Added Successfully')

                # Redirect to home page
                return redirect('home')

        # Render the add record page with the form
        return render(request, 'add_record.html', {'form': form})

    # If user is not authenticated
    else:

        # Send an error message
        messages.error(request, 'Please Login to Add Customer Records')

        # Redirect to home page
        return redirect('home')
