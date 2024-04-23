from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import uuid

class RegistrationForm(UserCreationForm):
    
    id = forms.CharField(required=True, max_length=36, widget=forms.TextInput(attrs={'placeholder': 'Enter your ID'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'id')
        
        
        