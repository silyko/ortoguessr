from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):

    signup_code = forms.CharField(label="Invitation code", max_length=50)

    def clean_signup_code(self):
        code = self.cleaned_data["signup_code"]
        if code.lower() != "pokercar":
            raise ValidationError("Invitation code not accepted!")
