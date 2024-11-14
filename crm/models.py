from django.db import models


# Create Record Model for CRM Application with fields for customer information
class Record(models.Model):

    # Define fields for the Record model
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)

    # Define a string representation for the Record model
    def __str__(self):
        return self.first_name + ' ' + self.last_name
