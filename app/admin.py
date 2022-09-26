from django.contrib import admin
from .models import CustomUser, UserFiles

admin.site.register(CustomUser)
admin.site.register(UserFiles)
