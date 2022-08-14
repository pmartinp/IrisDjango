from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myApp.form import CustomUserCreationform
from django.contrib.auth import login
from django.urls import reverse


@login_required
def home(request):
    return render(request,
                  'home.html',
                  context={'sepal_length': 5.1, 'sepal_width': 3.5,
                           'petal_length': 1.4, 'petal_width': 0.2,
                           'class': "Iris Setosa"})


def register(request):
    if request.method == "GET":
        return render(request, 
                        "registration/register.html",
                        {"form": CustomUserCreationform})
    elif request.method == "POST":
        form = CustomUserCreationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
