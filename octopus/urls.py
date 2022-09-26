from django.contrib import admin
from django.urls import path
from app.views import index, create_user, get_users, edit_user, delete_user, list_of_files, delete_file, add_file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/create', create_user, name='create_user'),
    path('users/list', get_users, name='lists'),
    path('users/edit/<int:id>/', edit_user, name='edit_user'),
    path('users/delete/<int:id>/', delete_user, name='delete_user'),
    path('files/list', list_of_files, name='list_of_files'),
    path('files/delete/<int:id>/', delete_file, name='delete_file'),
    path('files/add', add_file, name='add_file'),
    path('', index, name='index'),
]
