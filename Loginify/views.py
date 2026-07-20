from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import UserDetails
import json


def hello_world(request):
    return HttpResponse("Hello, world!")


@csrf_exempt
def signup(request):
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email:
            messages.error(request, "Username and email are required.")
            return render(request, "Loginify/signup.html")

        if UserDetails.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "Loginify/signup.html")

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "Loginify/signup.html")

        new_user = UserDetails(username=username, email=email, password=password)
        new_user.save()

        if request.content_type == "application/json":
            return JsonResponse({"message": "Signup successful"})

        return redirect("login")

    return render(request, "Loginify/signup.html")


@csrf_exempt
def login(request):
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        email = data.get("email")
        password = data.get("password")

        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            messages.error(request, "No account found with that email.")
            return render(request, "Loginify/login.html")

        if user.password == password:
            if request.content_type == "application/json":
                return JsonResponse({"message": "Login successful", "username": user.username})
            return render(request, "Loginify/success.html", {"username": user.username})
        else:
            messages.error(request, "Incorrect password.")
            return render(request, "Loginify/login.html")

    return render(request, "Loginify/login.html")


# below this is the CRUD stuff for postman (task 5)

def get_all_users(request):
    users = UserDetails.objects.all()
    data = []
    for u in users:
        data.append({"username": u.username, "email": u.email, "password": u.password})
    return JsonResponse({"users": data})


def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found"})
    return JsonResponse({"username": user.username, "email": user.email, "password": user.password})


@csrf_exempt
def update_user(request, email):
    user = UserDetails.objects.get(email=email)
    data = json.loads(request.body)

    if "email" in data:
        user.email = data["email"]
    if "password" in data:
        user.password = data["password"]

    user.save()
    return JsonResponse({"message": "User updated"})


@csrf_exempt
def delete_user(request, email):
    user = UserDetails.objects.get(email=email)
    user.delete()
    return JsonResponse({"message": "User deleted"})
