import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .models import UserDetails


# ---------------------------------------------------------------------------
# Task 2: Basic test view
# ---------------------------------------------------------------------------
def hello_world(request):
    """Simple view returning plain text for testing purposes."""
    return HttpResponse("Hello, world!")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _get_payload(request):
    """
    Return request data as a dict, supporting both HTML form posts
    (application/x-www-form-urlencoded) and raw JSON bodies (Postman).
    """
    if request.content_type and "application/json" in request.content_type:
        try:
            return json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return {}
    return request.POST


def _user_to_dict(user):
    return {
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }


# ---------------------------------------------------------------------------
# Task 3: Signup & Login (template rendering)
# ---------------------------------------------------------------------------
@csrf_exempt
def signup(request):
    """
    Handle user registration with name, email and password.
    Enforces unique email. On success redirects to the login page.
    """
    if request.method == "POST":
        data = _get_payload(request)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password", "")

        # Basic required-field validation
        if not username or not email:
            error = "Username and email are required."
            if request.content_type and "application/json" in request.content_type:
                return JsonResponse({"error": error}, status=400)
            messages.error(request, error)
            return render(request, "Loginify/signup.html")

        # Uniqueness checks
        if UserDetails.objects.filter(username=username).exists():
            error = "Username already exists."
            if request.content_type and "application/json" in request.content_type:
                return JsonResponse({"error": error}, status=400)
            messages.error(request, error)
            return render(request, "Loginify/signup.html")

        if UserDetails.objects.filter(email=email).exists():
            error = "Email already registered."
            if request.content_type and "application/json" in request.content_type:
                return JsonResponse({"error": error}, status=400)
            messages.error(request, error)
            return render(request, "Loginify/signup.html")

        UserDetails.objects.create(
            username=username, email=email, password=password
        )

        if request.content_type and "application/json" in request.content_type:
            return JsonResponse(
                {"message": "Signup successful", "username": username},
                status=201,
            )

        # Redirect to login page on successful signup
        return redirect("login")

    return render(request, "Loginify/signup.html")


@csrf_exempt
def login(request):
    """
    Handle login using email and password.
    On success, displays a success message.
    """
    if request.method == "POST":
        data = _get_payload(request)
        email = data.get("email")
        password = data.get("password", "")

        try:
            user = UserDetails.objects.get(email=email)
        except UserDetails.DoesNotExist:
            error = "No account found with that email."
            if request.content_type and "application/json" in request.content_type:
                return JsonResponse({"error": error}, status=404)
            messages.error(request, error)
            return render(request, "Loginify/login.html")

        if user.password == password:
            if request.content_type and "application/json" in request.content_type:
                return JsonResponse(
                    {"message": "Login successful", "username": user.username}
                )
            return render(
                request,
                "Loginify/success.html",
                {"username": user.username},
            )

        error = "Incorrect password."
        if request.content_type and "application/json" in request.content_type:
            return JsonResponse({"error": error}, status=401)
        messages.error(request, error)
        return render(request, "Loginify/login.html")

    return render(request, "Loginify/login.html")


# ---------------------------------------------------------------------------
# Task 5: CRUD operations (JSON API, tested via Postman)
# ---------------------------------------------------------------------------
def get_all_users(request):
    """READ: Retrieve and display details of all users."""
    users = list(UserDetails.objects.all().values("username", "email", "password"))
    return JsonResponse({"count": len(users), "users": users})


def get_user_by_email(request, email):
    """READ: Retrieve details of a specific user by email."""
    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)
    return JsonResponse(_user_to_dict(user))


@csrf_exempt
def update_user(request, email):
    """UPDATE: Update a user's details, located by email."""
    if request.method not in ("PUT", "PATCH", "POST"):
        return JsonResponse(
            {"error": "Use PUT/PATCH to update."}, status=405
        )

    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

    data = _get_payload(request)

    # Update email if provided and still unique
    new_email = data.get("email")
    if new_email and new_email != user.email:
        if UserDetails.objects.filter(email=new_email).exists():
            return JsonResponse(
                {"error": "That email is already in use."}, status=400
            )
        user.email = new_email

    if "password" in data:
        user.password = data.get("password", "")

    user.save()
    return JsonResponse(
        {"message": "User updated", "user": _user_to_dict(user)}
    )


@csrf_exempt
def delete_user(request, email):
    """DELETE: Delete a user by email."""
    if request.method != "DELETE":
        return JsonResponse({"error": "Use DELETE method."}, status=405)

    try:
        user = UserDetails.objects.get(email=email)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)

    username = user.username
    user.delete()
    return JsonResponse(
        {"message": f"User '{username}' deleted successfully."}
    )
