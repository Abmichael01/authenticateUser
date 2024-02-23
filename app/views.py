from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


def index(request):
    return redirect("login")

def verify_username(request):
    data = json.loads(request.body)
    username = data["username"]

    if not str(username).isalnum():
        return JsonResponse({
            "username_error": "usersame can only contain alphanumeric charaters"
        })
    
    if len(username) < 6:
        return JsonResponse({
            "username_error": "usersame cannot be less than 6 characters"
        })
    
    if User.objects.filter(username = username).exists():
        return JsonResponse({
            "username_error": "usersame in use, choose another username"
        })
    
    return JsonResponse({
            "username_valid": True
        })


def verify_email(request):
    data = json.loads(request.body)
    email = data["email"]

    if not validate_email(email):
        return JsonResponse({
            "email_error": "email is invalid"
        })
    
    if User.objects.filter(email = email).exists():
        return JsonResponse({
            "email_error": "email in use, choose another email"
        })
    
    return JsonResponse({
            "email_valid": True
        })



    
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("success")
        else:
            messages.error(request, "Username or password is incorrect")
        
    return render(request, "app/login.html")



def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        context = {
            "username": username,
            "email": email
        }

        if not User.objects.filter(username = username).exists():
            if not User.objects.filter(username = username).exists():
                if not password1 == password2:
                    messages.error(request, "Password does not match")
                    return render(request, "app/register.html", context)
                if len(password1) < 8: 
                    messages.error(request, "Password is too short")
                    return render(request, "app/register.html", context)
                
                user = User.objects.create_user(
                    username= username,
                    email= email,
                )
                user.set_password(password1)
                user.save()
                messages.success(request, "Account created successfully. Please login")

    return render(request, "app/register.html")


def success(request):
    return render(request, "app/success.html")

def  logout_user(request):
    logout(request)
    return redirect("login")
