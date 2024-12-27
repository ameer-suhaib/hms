from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Role

class RegistrationForm(UserCreationForm):
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'role']
