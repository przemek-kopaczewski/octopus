from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


#main page, without login you didn't see page
@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login/')
def register(request):
    return render(request, 'register_user.html')
