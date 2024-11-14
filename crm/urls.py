from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin
    path('', views.home, name='home'),  # home
    # path('login/', views.login_user, name='login'), # login
    path('logout/', views.logout_user, name='logout'),  # logout
    path('register/', views.register_user, name='register'),  # register
    path('record/<int:pk>', views.customer_record, name='record'),  # record

]
