from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin page
    path('', views.home, name='home'),  # home page
    # path('login/', views.login_user, name='login'), # login page
    path('logout/', views.logout_user, name='logout'),  # logout page
]
