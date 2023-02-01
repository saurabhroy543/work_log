from django import forms
from .models import User


class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'nameid'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'nameid'})
        }
