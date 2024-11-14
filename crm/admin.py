from django.contrib import admin  # Import Django's admin module to register models
from .models import Record  # Import the Record model from models.py

# Register the Record model with the Django admin site
admin.site.register(Record)
