from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import get_user_model
from .forms import CustomUserForm, UserFilesForm, UserCustomForm
from .models import CustomUser, UserFiles
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.views.generic import ListView
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    model = CustomUser
    template_name = 'register_user.html'
    form_class = UserCustomForm
    success_url = '/'
    permission_required = 'app.add_customuser'

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data.get('password'))
        form.save()
        return super(UserCreateView, self).form_valid(form)


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomUser
    template_name = 'list_user.html'
    permission_required = 'app.view_customuser'


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'change_user.html'
    form_class = UserCustomForm
    success_url = '/'
    permission_required = 'app.change_customuser'

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data.get('password'))
        form.save()
        return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser
    success_url = '/'
    template_name = 'delete_user.html'
    permission_required = 'app.delete_customuser'


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
