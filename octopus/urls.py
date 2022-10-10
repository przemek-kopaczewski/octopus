from django.contrib import admin
from django.urls import path
from app.views import index, UserCreateView, UserListView, UserUpdateView, UserDeleteView, list_of_files, delete_file,\
    add_file
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/create', UserCreateView.as_view(), name='create_user'),
    path('users/list', UserListView.as_view(), name='list_user'),
    path('users/edit/<pk>/', UserUpdateView.as_view(), name='change_user'),
    path('users/delete/<pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('files/list', list_of_files, name='list_of_files'),
    path('files/delete/<int:id>/', delete_file, name='delete_file'),
    path('files/add', add_file, name='add_file'),
    path('', index, name='index'),
]
