from django.forms import ModelForm
from .models import CustomUser, UserFiles


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'last_name', 'password', 'phone_number']


class UserFilesForm(ModelForm):
    class Meta:
        model = UserFiles
        fields = ['user_files']
