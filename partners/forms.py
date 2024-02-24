from django import forms
from .models import PartnerTag
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_recaptcha.fields import ReCaptchaField

# Form for creating new partner entries
class PartnerForm(forms.Form):
    # Fields for partner information
    name = forms.CharField(label="Name")
    description = forms.CharField(label="Description")
    logo = forms.ImageField(label="Logo", required=False)
    website = forms.URLField(label="Website", initial="https://")
    contact_email = forms.EmailField(label="Contact Email")
    contact_phone = forms.CharField(label="Contact Phone",)
    
    # Field for selecting multiple tags from the PartnerTag model
    tags = forms.ModelMultipleChoiceField(
        queryset=PartnerTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Tags",
    )
    
    # User authentication fields
    email = forms.EmailField(label="Admin Email")
    username = forms.CharField(label="Admin Username")
    password = forms.CharField(
        label="Admin Password", widget=forms.PasswordInput(), validators=[validate_password]
    )
    
    # ReCaptcha field for spam prevention
    captcha = ReCaptchaField()

# Form for adding new staff members to a partner
class PartnerStaffForm(forms.ModelForm):
    # Field for selecting staff role
    role = forms.ChoiceField(
        choices=(
            ("manager", "Manager"),
            ("editor", "Editor"),
        ),
        label="Role",
    )
    
    # User authentication fields
    email = forms.EmailField(label="Email", required=True)
    username = forms.CharField(label="Username")
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(), validators=[validate_password]
    )
    
    # Custom clean method to ensure unique username and email
    def clean(self):
        cleaned_data = super().clean()
        if "username" in cleaned_data and "email" in cleaned_data:
            # Check if there is already a user with the provided email and username
            current_user = User.objects.filter(
                username__iexact=cleaned_data["username"],
                email__iexact=cleaned_data["email"],
            ).first()
            curent_email = User.objects.filter(
                email__iexact=cleaned_data["email"],
            ).first()
            curent_username = User.objects.filter(
                username__iexact=cleaned_data["username"],
            ).first()
            
            # Add error messages if email or username already exist
            if curent_email:
                self.add_error("email", "Email already exists")
            if curent_username:
                self.add_error("username", "Username already exists")
            
            return cleaned_data
