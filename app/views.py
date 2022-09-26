from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import get_user_model
from .forms import CustomUserForm, UserFilesForm
from .models import CustomUser, UserFiles
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission


#main page, without login you didn't see page
@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login/')
@permission_required("app.add_customuser")
def create_user(request):
    form = CustomUserForm(request.POST or None)
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

    return render(request, 'register_user.html', {'form': form, 'new': True})


@login_required(login_url='login/')
@permission_required("app.view_customuser")
def get_users(request):
    user = get_user_model()
    all_users = user.objects.all()
    return render(request, 'list_user.html', {'all_users': all_users})


@login_required(login_url='login/')
@permission_required("app.change_customuser")
def edit_user(request, id):
    user = get_object_or_404(CustomUser, pk=id)
    form = CustomUserForm(request.POST, instance=user)
    permissions = Permission.objects.all()
    if form.is_valid():
        form.username = form.cleaned_data['username']
        form.name = form.cleaned_data['name']
        form.last_name = form.cleaned_data['last_name']
        form.phone_number = form.cleaned_data['phone_number']
        form.post_permission = request.POST.getlist('post_permission')
        for perm in form.post_permission:
            permission = Permission.objects.get(codename=perm)
            user.user_permissions.add(permission)
        user.set_password(form.cleaned_data['password'])
        form.save()
        return redirect(index)

    return render(request, 'register_user.html', {'form': form, 'new': False, 'permissions': permissions})


@login_required(login_url='login/')
@permission_required("app.delete_customuser")
def delete_user(request, id):
    user = get_object_or_404(CustomUser, pk=id)

    if request.method == "POST":
        user.delete()
        return redirect(index)

    return render(request, 'delete_user.html', {'user': user})


def add_file(request):
    form = UserFilesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        file = UserFiles(user_files=request.FILES['user_files'])
        file.save()
        return redirect(list_of_files)

    return render(request, 'add_file.html', {'form': form})


def list_of_files(request):
    files = UserFiles.objects.all()
    return render(request, 'list_of_files.html', {'all_files': files})


def delete_file(request, id):
    file = get_object_or_404(UserFiles, pk=id)

    if request.method == "POST":
        file.delete()
        return redirect(index)

    return render(request, 'delete_file.html', {'file': file})
