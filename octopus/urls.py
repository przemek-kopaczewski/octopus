from django.contrib import admin
from django.urls import path
from app.views import index, create_user, get_users, edit_user, delete_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_user/', create_user, name='create_user'),
    path('lists/', get_users, name='lists'),
    path('edit_user/<int:id>/', edit_user, name='edit_user'),
    path('delete/<int:id>/', delete_user, name='delete_user'),
    path('', index, name='index'),
]
