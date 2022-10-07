from django import forms
from .models import CustomUser, UserFiles


class UserFilesForm(forms.ModelForm):
    class Meta:
        model = UserFiles
        fields = ['user_files']


class UserCustomForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'last_name', 'password', 'phone_number')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'})
        }
