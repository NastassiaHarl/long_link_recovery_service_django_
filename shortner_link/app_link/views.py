from django.shortcuts import render, redirect
from . import models
from .forms import UserRegisterForm, UserAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import render
import uuid
from .models import LinkInfo
from django.http import HttpResponse


def info_users(request):
    users = models.Users.objects.all()
    context = {
        "users": users,
    }
    return render(request, "users.html", {"context": context})


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('users')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'registration.html', {"form": form})


def authorization(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users')
    else:
        form = UserAuthenticationForm()
    return render(request, 'authorization.html', {"form": form})


def users_logout(request):
    logout(request)
    return redirect(reverse("authorization"))


def add_link(request):
    if request.method == 'POST':
        original_link = request.POST['link']
        short_link = str(uuid.uuid4())[:5]
        new_link = LinkInfo(original_link=original_link, short_link=short_link)
        new_link.save()
        return HttpResponse(short_link)


def shorten_link(request, pk):
    short_link = LinkInfo.objects.get(short_link=pk)
    return redirect(short_link.link)


# def info_urls(request):
#     info_urls = models.LinkInfo.objects.all()
#     context = {
#         "info_urls": info_urls,
#     }
#     return render(request, "info_link.html", {"context": context})



def post(request):
    context = {
        'posts': models.Post.objects.filter(author=request.user)
    }
    return render(request, 'info_link.html', context)