# Import Django's built-in form for user creation
from django.contrib.auth.forms import UserCreationForm
# Import Django's built-in User model
from django.contrib.auth.models import User
from django import forms  # Import Django's forms module to customize form fields
from .models import Record  # Import the Record model from models.py

# Custom sign-up form that extends Django's UserCreationForm to include additional fields


class SignUpForm(UserCreationForm):

    # Custom email field with specific styling and placeholder
    email = forms.EmailField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    # Custom first_name field with specific styling and placeholder
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    # Custom last_name field with specific styling and placeholder
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    # Meta class to define model association and fields to include in the form
    class Meta:

        # Associates the form with the User model
        model = User

        # Specifies fields to display in the form
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

        # Customizes widgets for each field with classes and placeholders for styling
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

    # Constructor to customize form field attributes and labels
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customizes the username field with additional placeholder and help text
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        # Removes the label for a cleaner design
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        # Customizes the password1 field with a placeholder and detailed help text
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        # Removes the label for a cleaner design
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # Customizes the password2 field with a placeholder and help text to confirm password entry
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        # Removes the label for a cleaner design
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# Create Add Record Form for CRM Application with fields for customer information
class AddRecordForm(forms.ModelForm):
    # Custom form field for first_name with specific styling and placeholder
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First Name'}), label='')

    # Custom form field for last_name with specific styling and placeholder
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label='')

    # Custom form field for email with specific styling and placeholder
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}), label='')

    # Custom form field for phone with specific styling and placeholder
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone'}), label='')

    # Custom form field for address with specific styling and placeholder
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Address'}), label='')

    # Custom form field for city with specific styling and placeholder
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'City'}), label='')

    # Custom form field for state with specific styling and placeholder
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'State'}), label='')

    # Custom form field for zip_code with specific styling and placeholder
    zip_code = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Zip'}), label='')

    # Meta class to define model association and fields to include in the form
    class Meta:
        # Associates the form with the Record model
        model = Record
        # Specifies fields to display in the form (all fields from the Record model)
        exclude = ("user",)
