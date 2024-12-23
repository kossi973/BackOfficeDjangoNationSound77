from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import UserProfile
import re


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'address', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'rounded border-gray-300 p-2'}),
            'last_name': forms.TextInput(attrs={'class': 'rounded border-gray-300 p-2'}),
            'address': forms.Textarea(attrs={'class': 'rounded border-gray-300 p-2'}),
            'email': forms.EmailInput(attrs={'class': 'rounded border-gray-300 p-2'}),
        }


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'rounded-lg',
            'placeholder': 'Nom d\'utilisateur'
            })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-lg',
            'placeholder': 'Mot de passe'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')        
        if len(username) < 6:
            raise ValidationError('Le nom d\'utilisateur doit contenir au moins 6 caractères.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 10:
            raise ValidationError('Le mot de passe doit contenir au moins 10 caractères.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Le mot de passe doit contenir au moins un caractère spécial.')
        return password
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'rounded-lg',
            'placeholder': 'Nom d\'utilisateur'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'rounded-lg',
            'placeholder': 'Mot de passe'
        })
    )