from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from user.forms import (UserLoginForm, UserProfileChangeForm,
                        UserRegistrationForm,)


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("buildings:index"))
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "user/login.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:login"))
    else:
        form = UserRegistrationForm()
    context = {"form": form}
    return render(request, "user/registration.html", context=context)


def profile_change(request):
    if request.method == "POST":
        form = UserProfileChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = UserProfileChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "user/profile.html", context=context)


def logout(request):
    auth.logout(request)
    return redirect("buildings:index")
