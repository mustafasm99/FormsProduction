from django.shortcuts import render,redirect
from django.contrib.auth import login, logout , authenticate
from django.contrib import messages
# Create your views here.

def home(e):
    if e.method == "POST":
        username = e.POST.get("username")
        password = e.POST.get("password")
        user = authenticate(e , username=username , password = password)
        print(username , password , user)
        if user:
            login(e , user)
            return redirect("form:home")
        else: 
            messages.add_message(e , message="username or password are not correct ", level=messages.INFO ,extra_tags="error")

    return render(e , "authapp/home.html")