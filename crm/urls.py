# Description: This file contains the URL patterns for the CRM app, mapping views to specific URLs.
# Importing necessary modules and views for URL routing.
from django.urls import path
from django.contrib import admin
from . import views  # Import views from the current application to link with URL patterns

# Defining URL patterns for the CRM app.
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site path for backend management
    # Home page; renders the main page for logged-in users or redirects to login
    path('', views.home, name='home'),

    # Uncomment the following line if you want to enable login functionality via URL.
    # path('login/', views.login_user, name='login'), # Login page; handles user login

    # Logout page; logs out the user and redirects to home
    path('logout/', views.logout_user, name='logout'),
    # Register page; handles new user registration
    path('register/', views.register_user, name='register'),

    # Record Specific URLs
    # Detail page for a specific record; requires primary key (pk)
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record,
         name='delete_record'),  # Delete page; deletes specific record by primary key

]
