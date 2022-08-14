from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password


#main page, without login you didn't see page
@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login/')
def register(request):
    form = CustomUserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        password = make_password(form.cleaned_data['password'])
        phone_number = form.cleaned_data['phone_number']
        user = CustomUser(username=username, name=name, last_name=last_name, password=password, phone_number=phone_number)
        user.save()
        return redirect(index)

    return render(request, 'register_user.html', {'form' : form, 'new' : True})


def get_users(request):
    User = get_user_model()
    all_users = User.objects.all()
    return render(request, 'list_user.html', {'all_users' : all_users})


@login_required(login_url='login/')
def edit_user(request, id):
    User = get_object_or_404(CustomUser, pk=id)
    form = CustomUserForm(request.POST or None, instance=User)
    if form.is_valid():
        username = form.cleaned_data['username']
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        password = make_password(form.cleaned_data['password'])
        phone_number = form.cleaned_data['phone_number']
        user = CustomUser(username=username, name=name, last_name=last_name, password=password,
                          phone_number=phone_number)
        user.save()
        return redirect(index)

    return render(request, 'register_user.html', {'form': form, 'new' : False})


@login_required(login_url='login/')
def delete_user(request, id):
    User = get_object_or_404(CustomUser, pk=id)

    if request.method == "POST":
        User.delete()
        return redirect(index)

    return render(request, 'delete_user.html', {'user': User})
