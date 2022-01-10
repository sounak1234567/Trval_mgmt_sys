from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# create your views here


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) > 10:
            messages.add_message(request, messages.ERROR, "Username should not be more than 10 characters.")
            return redirect("home")
        if pass1 != pass2:
            messages.add_message(request, messages.ERROR, "Passwords do not mach.")
            return redirect("home")

        # creating our user

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.add_message(request, messages.SUCCESS, "Your account was created successfully!")
        return redirect("home")
    else:
        return HttpResponse("404 - error code")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username1']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.add_message(request, messages.SUCCESS, f"Hello {fname}!")
            return redirect("home")
        else:
            return HttpResponse("User does not exist.")
