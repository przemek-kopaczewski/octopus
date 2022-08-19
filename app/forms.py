from django.forms import ModelForm
from .models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'last_name', 'password', 'phone_number']
